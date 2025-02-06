from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardMarkup

from bot.configs import admin_settings
from bot.entities.category import Category


class Keyboard:

    @staticmethod
    def get_main_menu_keyboard():
        keyboard = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        keyboard.add(admin_settings.language.catalog)
        return keyboard

    @staticmethod
    def get_catalog_keyboard(categories: list[Category], parent_id: str):
        keyboard = InlineKeyboardMarkup(row_width=1)
        for category in categories:
            keyboard.add(
                InlineKeyboardButton(
                    category.name,
                    callback_data=
                    f"category_id:{category.id}:{category.parent_category_id}"
                )
            )
        if not categories or categories[0].parent_category_id != "":
            keyboard.add(
                InlineKeyboardButton(
                    text="Назад", callback_data=f"category_id:back:{parent_id}"
                )
            )
        return keyboard
