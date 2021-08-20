# Getting Started

Here is an example:

```python
import asyncio
import os

from jetblack_tweeter import Tweeter
from jetblack_tweeter.clients.bareclient import BareTweeterSession

# Get the secrets from environment variables.
APP_KEY = os.environ["APP_KEY"]
APP_KEY_SECRET = os.environ["APP_KEY_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]


async def main():
    tweeter = Tweeter(
        BareTweeterSession(),
        APP_KEY,
        APP_KEY_SECRET,
        # Optional for user authentication.
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )

    user_timeline = await tweeter.statuses.user_timeline()
    print(user_timeline)

    account_settings = await tweeter.account.settings()
    print(account_settings)

    account_verify_credentials = await tweeter.account.verify_credentials()
    print(account_verify_credentials)

    # Watch the random sampling of tweets chosen by twitter
    async for tweet in tweeter.stream.sample():
        print(tweet)

    # Stream tweets which have the tag "#python" from New York
    # and San Francisco.
    async for tweet in tweeter.stream.filter(
            track=['#python'],
            locations=[
                ((-122.75, 36.8), (-121.75, 37.8)),
                ((-74, 40), (-73, 41))
            ]
    ):
        print(tweet)

    result = await tweeter.statuses.update('Hello from jetblack-tweeter')
    print(result)

    # Close the tweeter.
    await tweeter.close()

if __name__ == '__main__':
    asyncio.run(main())
```

This example uses `aiohttp` with context management.

```python
import asyncio
import os

from jetblack_tweeter import Tweeter
from jetblack_tweeter.clients.aiohttp import AiohttpTweeterSession

async def main():
    async with Tweeter(
        AiohttpTweeterSession(),
        # required for oauth1 signing:
        os.environ["APP_KEY"],
        os.environ["APP_KEY_SECRET"],
        # optionally necessary for endpoints requiring a user's scope:
        access_token=os.environ["ACCESS_TOKEN"],
        access_token_secret=os.environ["ACCESS_TOKEN_SECRET"]
    ) as tweeter:

        user_timeline = await tweeter.statuses.user_timeline()
        print(user_timeline)

if __name__ == '__main__':
    asyncio.run(main())

```
