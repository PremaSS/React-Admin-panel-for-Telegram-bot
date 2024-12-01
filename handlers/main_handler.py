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

# Example of file
# CQACAgIAAxkBAAIugmcuUHKJ8KobEBsEpVQ03q44az1AAAI-YQAC2utwSfcPRT_V5fQBNgQ
# "audio" : {
#     "duration" : 707,
#     "file_name" : "Выборы_в_США_кто_победит,_11_октября_2024,_14388.mp3",
#     "mime_type" : "audio/mpeg",
#     "title" : "Выборы в США: кто победит?",
#     "performer" : "Е.С. Бхакти Викаша Свами",
#     "file_id" : "CQACAgIAAxkBAAIuemcpMCHgpp9PK49lH9oBQA56m-BvAAJwYgACakVISZq7QTppnA6cNgQ",
#     "file_unique_id" : "AgADcGIAAmpFSEk",
#     "file_size" : 11845404
#   }
