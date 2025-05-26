from aiogram import Dispatcher, Bot, types
from aiogram.dispatcher import filters

from bot.configs import admin_settings
from bot.handlers.main_handler import MainHandler
from bot.utils.metaclasses import ThreadSafeSingletonMeta


class HandlerRegistrar(metaclass=ThreadSafeSingletonMeta):

    def __init__(self, dispatcher: Dispatcher = None, bot: Bot = None):
        if None in (dispatcher, bot):
            raise TypeError("__init__() missing required positional arguments")
        self.dp = dispatcher
        self.main_handler = MainHandler()

    def register_handlers(self):
        self.dp.register_message_handler(
            self.main_handler.start_handler, commands=['start']
        )
        self.dp.register_message_handler(
            self.main_handler.open_catalog_handler,
            filters.Text(equals=admin_settings.language.catalog)
        )
        self.dp.register_callback_query_handler(
            self.main_handler.catalog_handler,
            filters.Text(startswith="category_id:")
        )
        self.dp.register_message_handler(
            self.main_handler.upload_audio_handler,
            content_types=types.ContentType.AUDIO
        )
        self.dp.register_message_handler(
            self.main_handler.upload_photo_handler,
            content_types=[types.ContentType.PHOTO]
        )

        self.dp.register_message_handler(
            self.main_handler.upload_video_handler,
            content_types=[types.ContentType.VIDEO]
        )
