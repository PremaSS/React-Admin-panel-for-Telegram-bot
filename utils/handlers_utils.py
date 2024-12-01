import logging

from aiogram import Bot
from aiogram.types import InputFile

from utils.metaclasses import SingletonMeta


class HandlersUtils(metaclass=SingletonMeta):

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    async def get_photo_from_file_id(self, file_id):
        try:
            file_info = await self.bot.get_file(file_id)
            url = await file_info.get_url()
            file = InputFile.from_url(url)
        except Exception as e:
            logging.error(e)
            return None
        return file
