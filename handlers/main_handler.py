from aiogram import types

from configs import admin_settings
from handlers.base_handler import BaseProjectHandler
from keyboard.admin_change_order_state_keyboard import \
    Keyboard
from transactions.main_transactions import Transactions


class MainHandler(BaseProjectHandler):
    transactions = Transactions()

    @staticmethod
    async def start_handler(message: types.Message):
        await message.answer(
            admin_settings.language.catalog,
            reply_markup=Keyboard.get_main_menu_keyboard()
        )

    async def open_catalog_handler(self, message: types.Message):
        categories = self.transactions.get_catalog("")
        keyboard = Keyboard.get_catalog_keyboard(
            categories=categories, parent_id=""
        )
        await message.answer(
            admin_settings.language.catalog, reply_markup=keyboard
        )

    async def catalog_handler(self, callback: types.CallbackQuery):
        category_id = callback.data.split(":")[1]
        parent_id = callback.data.split(":")[2]
        if category_id == "back":
            categories = self.transactions.get_catalog(parent_id)
        else:
            categories = self.transactions.get_catalog(category_id)
        parent = self.transactions.get_parent_id_by_category_id(
            categories[0].parent_category_id
        ) if category_id == "back" else parent_id

        await callback.message.edit_reply_markup(
            reply_markup=Keyboard.get_catalog_keyboard(
                categories=categories,
                parent_id=parent
            )
        )

    async def upload_audio_handler(self, message: types.Message):
        audio = message.audio
        file_id = audio.file_id
        duration = audio.duration
        file_name = audio.file_name
        mime_type = audio.mime_type
        title = audio.title
        performer = audio.performer
        file_unique_id = audio.file_unique_id
        file_size = audio.file_size
        self.transactions.add_audio(
            file_id, duration, file_name, mime_type, title, performer,
            file_unique_id, file_size
        )
        await message.answer(admin_settings.language.audio_uploaded)
