import logging
from typing import Iterable

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

    @staticmethod
    def chunker(iterable: Iterable, chunk_size: int):
        """Create list of chunks with specific chunk_size from Iterable.
        For example:
        chunker([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) -> [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        """  # noqa
        d = {}
        for i, x in enumerate(iterable):
            d.setdefault(i // chunk_size, []).append(x)
        return list(d.values())
