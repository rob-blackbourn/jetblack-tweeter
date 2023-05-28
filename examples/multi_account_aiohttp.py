"""An example using aiohttp and multiple accounts"""

import asyncio
from asyncio import Queue, Event
from datetime import datetime, timedelta
import os
from typing import Any, Dict

from jetblack_tweeter import Tweeter, ApiError
from jetblack_tweeter.clients.aiohttp import AiohttpTweeterSession

class TimelineMessage:

    def __init__(self, tweet: Dict[str, Any]) -> None:
        self.screen_name = tweet['user'].get('screen_name','')
        self.author_id = tweet.get('author_id','')
        self.user_id = tweet['user']['id']
        self.text = tweet['text']
        self.created_at = datetime.strptime(
            tweet['created_at'],
            "%a %b %d %H:%M:%S %z %Y"
        ).astimezone()

    def __str__(self) -> str:
        return "{screen_name} {author_id} {user_id} {text} {created_at}".format(
            screen_name = self.screen_name,
            author_id=self.author_id,
            user_id = self.user_id,
            text=self.text,
            created_at = self.created_at
        )

async def send_sms(text: str) -> None:
    print(f"Sending SMS {text}")
    # Fake up sending the texts with a sleep.
    await asyncio.sleep(1)
    print("Sent SMS")

async def send_texts_async(queue: Queue, stop_event: Event) -> None:

    while not stop_event.is_set():
        try:
            text = await asyncio.wait_for(queue.get(), timeout=1)
            await send_sms(text)
        except asyncio.TimeoutError:
            # We use a timeout so we can check the stop event.
            pass

    # Ensure all queued messages have been sent.
    while not queue.empty():
        text = await asyncio.wait_for(queue.get(), timeout=1)
        await send_sms(text)

def create_tweeters() -> Dict[str, Tweeter]:
    # Get the account data from environment variables.
    # This assumes the environment variables look as
    # follows (using TOM as an example):
    #
    #     export TOM_APP_KEY="******"
    #     export TOM_APP_KEY_SECRET="******"
    #     export TOM_BEARER_TOKEN="******"
    #     export TOM_ACCESS_TOKEN="******"
    #     export TOM_ACCESS_TOKEN_SECRET="******"
    #
    accounts = ("TOM", "DICK", "HARRY", "MARY")
    tweeters = {
        name: Tweeter(
            AiohttpTweeterSession(),
            os.environ[name + "_APP_KEY"],
            os.environ[name + "_APP_KEY_SECRET"],
            access_token=os.environ[name + "_ACCESS_TOKEN"],
            access_token_secret=os.environ[name + "_ACCESS_TOKEN_SECRET"]
        )
        for name in accounts
    }
    return tweeters

async def gather_tweets_async(queue: Queue, stop_event: Event) -> None:
    tweeters = create_tweeters()

    # Get all the screen names.
    screen_names: Dict[str, str] = {}
    for name, tweeter in tweeters.items():
        credentials = await tweeter.account.verify_credentials()
        screen_name = credentials['screen_name']
        print(f"{name}: {screen_name}")
        screen_names[name] = screen_name

    for name, tweeter in tweeters.items():

        current_screen_name = screen_names[name]

        print(f'Using account {name} ({current_screen_name})')

        for screen_name in screen_names.values():

            print(f'Getting user timeline for {screen_name}')

            try:
                user_timeline = await tweeter.statuses.user_timeline(
                    screen_name=screen_name,
                    trim_user=False,
                    count=20,
                    timeout=1
                )
                messages = [
                    TimelineMessage(tweet)
                    for tweet in user_timeline
                ]
                threshold = datetime.now().astimezone() - timedelta(days=5)
                message_text = '\n'.join(
                    str(message)
                    for message in messages
                    if message.created_at > threshold
                )
                if message_text:
                    # Stick the message on the queue for the SMS text
                    # task to send it.
                    await queue.put(message_text)
            except ApiError as error:
                print("Failed to read timeline", error)

    for tweeter in tweeters.values():
        await tweeter.close()

    print("Stopped gathering messages")

    stop_event.set()

async def main_async():
    # We will put the tweets on a queue. The SMS task will send them.
    queue = Queue()
    # We use an event to stop everything gracefully.
    stop_event = Event()

    # Wait for both gathering the tweets and sending the texts.
    await asyncio.wait(
        [
            gather_tweets_async(queue, stop_event),
            send_texts_async(queue, stop_event)
        ],
        return_when=asyncio.ALL_COMPLETED
    )

if __name__ == '__main__':
    asyncio.run(main_async())
