import asyncio
import os

from jetblack_tweeter import Tweeter
from jetblack_tweeter.clients.aiohttp import AiohttpTweeterSession


async def main():
    tweeter = Tweeter(
        AiohttpTweeterSession(),
        os.environ["APP_KEY"],
        os.environ["APP_KEY_SECRET"],
        access_token=os.environ["ACCESS_TOKEN"],
        access_token_secret=os.environ["ACCESS_TOKEN_SECRET"]
    )

    params = [
        'paulg',
        'evhead',
        'jack',
        'robblackbourn'
    ]
    for name in params:
        timeline = await tweeter.statuses.user_timeline(screen_name=name, include_rts=False)
        print(f"{name}: {len(timeline)}")
    print('done')

if __name__ == '__main__':
    asyncio.run(main())
