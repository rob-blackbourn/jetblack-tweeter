import asyncio
import os
from os.path import expandvars

from jetblack_tweeter import Tweeter
from jetblack_tweeter.bareclient import BareTweeterSession

CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]


async def main():
    tweeter = Tweeter(
        BareTweeterSession(),
        # required for oauth1 signing:
        CONSUMER_KEY,
        CONSUMER_SECRET,
        # optionally necessary for endpoints requiring a user's scope:
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )

    # user_timeline = await tweeter.user_timeline()
    # print(user_timeline)

    # account_settings = await tweeter.account_settings()
    # print(account_settings)

    # account_verify_credentials = await tweeter.account_verify_credentials()
    # print(account_verify_credentials)

    # watch the random sampling of tweets chosen by twitter
    async for tweet in tweeter.sample():
        print(tweet)

if __name__ == '__main__':
    asyncio.run(main())
