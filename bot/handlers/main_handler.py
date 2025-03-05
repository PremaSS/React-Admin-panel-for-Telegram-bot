from aiogram import types
from aiogram.types import InputMediaPhoto
from django.template.context_processors import media

from bot.configs import admin_settings
from bot.handlers.base_handler import BaseProjectHandler
from bot.keyboard.main_keyboard import Keyboard
from bot.transactions.main_transactions import Transactions
from bot.utils.handlers_utils import HandlersUtils


class MainHandler(BaseProjectHandler):
    transactions = Transactions()

    async def start_handler(self, message: types.Message):
        await message.answer(
            admin_settings.language.catalog,
            reply_markup=Keyboard.get_main_menu_keyboard()
        )
        user = message.from_user
        self.transactions.add_user_if_not_exist(
            user.id, user.username, user.full_name
        )

    async def open_catalog_handler(self, message: types.Message):
        categories = self.transactions.get_catalog("")
        keyboard = Keyboard.get_catalog_keyboard(
            categories=categories, parent_id=""
        )
        category_photo = self.transactions.get_category_photo("")
        await message.answer_photo(
            photo=category_photo,
            caption=admin_settings.language.catalog, reply_markup=keyboard
        )

    async def catalog_handler(self, callback: types.CallbackQuery):
        category_id_to_open = callback.data.split(":")[1]
        categories = self.transactions.get_catalog(category_id_to_open)
        parent_category_id = self.transactions.get_parent_id_by_category_id(
            category_id_to_open
        )
        if category_id_to_open == "":
            catalog_title = admin_settings.language.catalog
        else:
            catalog_title = self.transactions.get_category_by_id(
                category_id_to_open
            ).name

        media_files = self.transactions.get_media_by_category_id(
            category_id_to_open
        )
        category_photo = self.transactions.get_category_photo(category_id_to_open)
        if media_files:
            await callback.message.edit_caption(catalog_title)
            media_chunks = HandlersUtils.chunker(media_files, 10)
            for slice_media in media_chunks:
                await callback.message.answer_media_group(list(slice_media))

            await callback.message.answer_photo(
                photo=category_photo, caption=catalog_title,
                reply_markup=Keyboard.get_catalog_keyboard(
                    categories=categories,
                    parent_id=parent_category_id
                )
            )
        else:
            if not callback.message.photo[-1].file_id == category_photo:
                await callback.message.edit_media(
                    media=InputMediaPhoto(category_photo),
                    reply_markup=Keyboard.get_catalog_keyboard(
                        categories=categories,
                        parent_id=parent_category_id
                    )
                )
            await callback.message.edit_caption(
                catalog_title,
                reply_markup=Keyboard.get_catalog_keyboard(
                    categories=categories,
                    parent_id=parent_category_id
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
        self.transactions.add_media(
            file_id, duration, file_name, mime_type, title, performer,
            file_unique_id, file_size
        )
        await message.answer(admin_settings.language.audio_uploaded)

    async def upload_video_handler(self, message: types.Message):
        video = message.video
        file_id = video.file_id
        duration = video.duration
        file_name = video.file_name
        mime_type = video.mime_type
        file_unique_id = video.file_unique_id
        file_size = video.file_size
        self.transactions.add_media(
            file_id, duration, file_name, mime_type, None, None,
            file_unique_id, file_size
        )
        await message.answer(admin_settings.language.video_uploaded)

    async def upload_photo_handler(self, message: types.Message):
        updated_rows = self.transactions.add_photo(message.photo[-1].file_id)
        text = f"{admin_settings.language.photos_added}: {updated_rows}"
        await message.answer(text)
