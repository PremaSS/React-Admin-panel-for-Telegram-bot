from typing import Union

from cachetools.func import ttl_cache

from data_base.db import MainDataBase
from entities.category import Category
from utils.metaclasses import SingletonMeta


class Transactions(metaclass=SingletonMeta):
    data_base = MainDataBase()

    @ttl_cache(ttl=5 * 60)
    def get_catalog(self, parent_category_id: Union[int, str]) -> list[Category]:
        categories = self.data_base.get_catalog_by_parent_category_id(
            parent_category_id
        )
        return [Category(*category) for category in categories]

    @ttl_cache(ttl=5 * 60)
    def get_parent_id_by_category_id(self, category_id: str) -> int:
        response = self.data_base.get_parent_id_by_category_id(category_id)
        return response[0] if response else ''

    @ttl_cache(ttl=5 * 60)
    def add_audio(self, file_id: str, duration: int, file_name: str,
                  mime_type: str, title: str, performer: str,
                  file_unique_id: str, file_size: int):
        self.data_base.add_audio(
            file_id, duration, file_name, mime_type, title, performer,
            file_unique_id, file_size
        )
