import asyncio
import logging
import os
import platform

from dotenv import load_dotenv

from bot.initializer import Initializer

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
load_dotenv(".env", override=True)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DJANGO_DIR = os.path.join(BASE_DIR, "admin_project")
python_executable = "py" if platform.system() == "Windows" else "python3"


async def run_django():
    """Запуск Django-сервера из virtualenv"""
    django_url = f"0.0.0.0:{os.getenv('DJANGO_PORT')}"
    await asyncio.create_subprocess_exec(
        python_executable, "manage.py", "runserver", django_url, cwd=DJANGO_DIR,
    )


async def start():
    """Запускает Django и бота параллельно"""
    initializer = Initializer()

    django_task = asyncio.create_task(run_django())  # Django
    bot_task = asyncio.create_task(initializer.dp.start_polling())  # Бот

    await asyncio.gather(django_task, bot_task)

if __name__ == "__main__":
    asyncio.run(start())
