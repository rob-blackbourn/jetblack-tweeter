"""An example using bareClient"""

import asyncio
import os

from jetblack_tweeter import Tweeter
from jetblack_tweeter.clients.aiohttp import AiohttpTweeterSession


async def main():
    tweeters = {
        name: Tweeter(
            AiohttpTweeterSession(),
            os.environ[name + "_APP_KEY"],
            os.environ[name + "_APP_KEY_SECRET"],
            access_token=os.environ[name + "_ACCESS_TOKEN"],
            access_token_secret=os.environ[name + "_ACCESS_TOKEN_SECRET"]
        )
        for name in ("RB1", "RB2", "RB3", "RB4")
    }

    for name, tweeter in tweeters.items():

        print(f'User: {name}')

        credentials = await tweeter.account.verify_credentials()
        print(f"{name}: {credentials['screen_name']}")

        user_timeline = await tweeter.statuses.user_timeline(
            screen_name=credentials['screen_name'],
            trim_user=False
        )
        print(user_timeline)

        # lookup_tweets = await tweeter.statuses.lookup(ids=[1313175713030209536])
        # print(lookup_tweets)

        # search_results = await tweeter.search.tweets('python', count=5)
        # print(search_results)

        # account_settings = await tweeter.account.settings()
        # print(account_settings)

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

    for tweeter in tweeters.values():
        await tweeter.close()

if __name__ == '__main__':
    asyncio.run(main())
