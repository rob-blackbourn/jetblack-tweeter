import asyncio
import os

from jetblack_tweeter import Tweeter
from jetblack_tweeter.clients.aiohttp import AiohttpTweeterSession


async def run_stream(tweeter: Tweeter, name, track, locations) -> None:
    async for tweet in tweeter.stream.filter(track=track, locations=locations):
        print(f"{name}: {tweet['text']}")


async def main():
    tweeter = Tweeter(
        AiohttpTweeterSession(),
        os.environ["APP_KEY"],
        os.environ["APP_KEY_SECRET"],
        access_token=os.environ["ACCESS_TOKEN"],
        access_token_secret=os.environ["ACCESS_TOKEN_SECRET"]
    )

    params = [
        ('PYTHON', ['#python'], [((-122.75, 36.8), (-121.75, 37.8))]),
        ('JAVA', ['#java'], [((-122.75, 36.8), (-121.75, 37.8))]),
        ('CSHARP', ['#csharp'], [((-122.75, 36.8), (-121.75, 37.8))]),
    ]

    tasks = {
        asyncio.create_task(run_stream(tweeter, name, track, locations))
        for name, track, locations in params
    }

    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())
