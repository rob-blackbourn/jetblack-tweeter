"""An example using bareClient"""

import asyncio
from datetime import datetime
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

    me = await tweeter.users.me()
    timeline = await tweeter.users.timeline(me['data']['id'])
    rob = await tweeter.users.lookup_by_username('robblackbourn')
    following = await tweeter.users.following(me['data']['id'])
    followers = await tweeter.users.followers(me['data']['id'])

    rob2 = await tweeter.users.lookup_by_username('robblackbourn2')
    rob1 = await tweeter.users.lookup_by_username('robblackbourn1')
    rob = await tweeter.users.lookup_by_username('robblackbourn')

    liked_tweets = await tweeter.users.liked_tweets('44196397')

    user_timeline = await tweeter.statuses.user_timeline(screen_name='cali_student')
    # user_timeline = await tweeter.statuses.user_timeline(
    #     screen_name='cali_student',
    #     user_id = '1137278362',
    #     include_rts=False
    # )
    user_timeline = await tweeter.statuses.user_timeline(screen_name="robblackbourn1")
    user_timeline = await tweeter.statuses.user_timeline(screen_name="elonmusk")
    user_timeline = await tweeter.statuses.user_timeline(
        user_id='44196397'
    )

    user_timeline = await tweeter.statuses.user_timeline(
        user_id='44196397'
    )

    user_timeline = await tweeter.statuses.user_timeline()
    print(user_timeline)

    # lookup_tweets = await tweeter.statuses.lookup(ids=[1313175713030209536])
    # print(lookup_tweets)

    # search_results = await tweeter.search.tweets('python', count=5)
    # print(search_results)

    # account_settings = await tweeter.account.settings()
    # print(account_settings)

    # account_verify_credentials = await tweeter.account.verify_credentials()
    # print(account_verify_credentials)

    # watch the random sampling of tweets chosen by twitter
    # async for tweet in tweeter.stream.sample():
    #     print(tweet)

    # async for tweet in tweeter.stream.filter(
    #         track=['#python'],
    #         locations=[
    #             ((-122.75, 36.8), (-121.75, 37.8)),
    #             ((-74, 40), (-73, 41))
    #         ],

    # ):
    #     print(tweet['text'])

    # result = await tweeter.statuses.update('Test message')
    # print(result)

    await tweeter.close()

if __name__ == '__main__':
    asyncio.run(main())
