"""An example using bareClient"""

import asyncio
import os

from jetblack_tweeter import Tweeter
from jetblack_tweeter.clients.bareclient import BareTweeterSession

APP_KEY = os.environ["APP_KEY"]
APP_KEY_SECRET = os.environ["APP_KEY_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]


async def main():
    tweeter = Tweeter(
        BareTweeterSession(),
        # required for oauth1 signing:
        APP_KEY,
        APP_KEY_SECRET,
        # optionally necessary for endpoints requiring a user's scope:
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )

    user_timeline = await tweeter.statuses.user_timeline()
    print(user_timeline)

    # account_verify_credentials = await tweeter.account.verify_credentials()
    # print(account_verify_credentials)

    # lookup_tweets = await tweeter.statuses.lookup(ids=[1313175713030209536])
    # print(lookup_tweets)

    # search_results = await tweeter.search.tweets('python', count=5)
    # print(search_results)

    # account_settings = await tweeter.account.settings()
    # print(account_settings)

    # # watch the random sampling of tweets chosen by twitter
    # async for tweet in tweeter.stream.sample():
    #     print(tweet)

    # async for tweet in tweeter.stream.filter(
    #         track=['#python'],
    #         locations=[
    #             ((-122.75, 36.8), (-121.75, 37.8)),
    #             ((-74, 40), (-73, 41))
    #         ]
    # ):
    #     print(tweet)

    # result = await tweeter.statuses.update('Test message')
    # print(result)

    await tweeter.close()

if __name__ == '__main__':
    asyncio.run(main())
