from aiogram import types
from aiogram.utils.exceptions import MessageError

from utils.metaclasses import SingletonMeta


class BaseProjectHandler(metaclass=SingletonMeta):

    @staticmethod
    async def delete_or_set_deleted_text(message: types.Message):
        try:
            await message.delete()
        except (MessageError, TypeError):
            if message.photo:
                await message.edit_caption("Deleted")
            else:
                await message.edit_text("Deleted")
