import asyncio
import logging
import subprocess
import os

from bot.initializer import Initializer

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DJANGO_DIR = os.path.join(BASE_DIR, "admin_project")
PYTHON_PATH = os.path.join(BASE_DIR, "venv", "Scripts", "python.exe")

async def run_django():
    """Запуск Django-сервера из virtualenv"""
    process = await asyncio.create_subprocess_exec(
        PYTHON_PATH, "manage.py", "runserver", "127.0.0.1:8000",
        cwd=DJANGO_DIR,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    while True:
        line = await process.stdout.readline()
        if not line:
            break
        print(f"[Django] {line.decode().strip()}")

    # Вывод ошибок Django (если есть)
    stderr = await process.stderr.read()
    if stderr:
        print(f"[Django ERROR] {stderr.decode().strip()}")

async def start():
    """Запускает Django и бота параллельно"""
    initializer = Initializer()

    django_task = asyncio.create_task(run_django())  # Django
    bot_task = asyncio.create_task(initializer.dp.start_polling())  # Бот

    await asyncio.gather(django_task, bot_task)

if __name__ == "__main__":
    asyncio.run(start())

