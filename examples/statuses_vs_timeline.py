"""An example of status vs users for timeline"""

import asyncio
import os

from jetblack_tweeter import Tweeter
from jetblack_tweeter.clients.aiohttp import AiohttpTweeterSession

APP_KEY = os.environ["APP_KEY"]
APP_KEY_SECRET = os.environ["APP_KEY_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]


async def main():
    tweeter = Tweeter(
        AiohttpTweeterSession(ssl=False),
        # required for oauth1 signing:
        APP_KEY,
        APP_KEY_SECRET,
        # optionally necessary for endpoints requiring a user's scope:
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )

    # The Twitter username.
    # The "statuses" end point has developed issues with protected users.
    # Try a protected user!
    name = 'elonmusk'
    try:
        # Get the timeline with the old call. This may fail for a protected
        # user account, even if you are authorized.
        timeline1 = await tweeter.statuses.user_timeline(
            screen_name=name,
            include_rts=False
        )
        for tweet in timeline1:
            print(tweet['text'], tweet['created_at'])

        print("It worked")
    except:
        print("It failed")

    try:
        # This should work for protected users, if you have authorization.
        user = await tweeter.users.lookup_by_username(name)
        user_id = user['data']['id']
        timeline2 = await tweeter.users.timeline(
            user_id,
            exclude=['retweets', 'replies'],
            tweet_fields=['created_at']
        )
        for tweet in timeline2['data']:
            print(tweet['text'], tweet['created_at'])
        print("It worked")
    except:
        print("It failed")

    await tweeter.close()

if __name__ == '__main__':
    asyncio.run(main())
