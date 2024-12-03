from os import environ

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from configs import admin_settings
from configs.ukr import Ukrainian


class Initializer:

    def __init__(self) -> None:
        self.bot = Bot(token=environ['BOT_TOKEN'], parse_mode="HTML")
        self.dp = Dispatcher(self.bot, storage=MemoryStorage())

        self.__set_configs()
        self.__register_handlers(self.bot, self.dp)

    @staticmethod
    def __register_handlers(bot: Bot, dp: Dispatcher):
        from handler_registrars import HandlerRegistrar
        handler_registrar = HandlerRegistrar(dp, bot)

        handler_registrar.register_handlers()

    @staticmethod
    def __set_configs():
        """Set some initial configs"""
        admin_settings.language = Ukrainian()
