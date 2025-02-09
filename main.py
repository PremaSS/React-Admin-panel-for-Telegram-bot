import asyncio
import logging
import os

from bot.initializer import Initializer

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DJANGO_DIR = os.path.join(BASE_DIR, "admin_project")


async def run_django():
    """Запуск Django-сервера из virtualenv"""
    process = await asyncio.create_subprocess_exec(
        "python3", "manage.py", "runserver", "127.0.0.1:8000",
        cwd=DJANGO_DIR,
    )


async def start():
    """Запускает Django и бота параллельно"""
    initializer = Initializer()

    django_task = asyncio.create_task(run_django())  # Django
    bot_task = asyncio.create_task(initializer.dp.start_polling())  # Бот

    await asyncio.gather(django_task, bot_task)

if __name__ == "__main__":
    asyncio.run(start())

