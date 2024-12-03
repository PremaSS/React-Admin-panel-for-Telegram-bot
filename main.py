import asyncio
import logging

from initializer import Initializer

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


async def start() -> None:
    initializer = Initializer()
    await asyncio.gather(initializer.dp.start_polling())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start())
