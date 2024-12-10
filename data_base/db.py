import os
from typing import Union

from mysql import connector

from utils.metaclasses import SingletonMeta


class AbstractDataBase(metaclass=SingletonMeta):
    HOST = os.getenv("HOST")
    PORT = os.getenv("PORT")
    USER = os.getenv("USER")
    PASSWORD = os.getenv("PASSWORD")
    DATABASE = os.getenv("DATABASE")

    connection = connector.connect(
        host=HOST, port=PORT, user=USER, password=PASSWORD, database=DATABASE
    )


class MainDataBase(AbstractDataBase):

    def get_catalog_by_parent_category_id(self, parent_category_id):
        sql = "SELECT name, id, parent_category_id FROM category WHERE parent_category_id=%s"  # noqa
        self.connection.reconnect(attempts=2)
        with self.connection.cursor() as cursor:
            cursor.execute(sql, (parent_category_id,))
            return cursor.fetchall()

    def get_parent_id_by_category_id(self, category_id):
        sql = "SELECT parent_category_id FROM category WHERE id=%s"
        self.connection.reconnect(attempts=2)
        with self.connection.cursor() as cursor:
            cursor.execute(sql, (category_id,))
            return cursor.fetchone()

    def add_audio(self, file_id: str, duration: int, file_name: str,
                  mime_type: str, title: str, performer: str,
                  file_unique_id: str, file_size: int):
        sql = ("INSERT INTO audio(file_id, duration, file_name, mime_type,"
               " title, performer, file_unique_id, file_size) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
        self.connection.reconnect(attempts=2)
        with self.connection.cursor() as cursor:
            cursor.execute(
                sql,
                (file_id, duration, file_name, mime_type, title, performer,
                file_unique_id, file_size)
            )
            self.connection.commit()

    def add_user_if_not_exist(self, tg_user_id: Union[int, str], username: str,
                              full_name: str):
        sql = """INSERT IGNORE INTO `user` 
        SET `tg_user_id` = %s, `username` = %s, `full_name` = %s;"""
        self.connection.reconnect(attempts=2)
        with self.connection.cursor() as cursor:
            cursor.execute(sql, (tg_user_id, username, full_name))
            self.connection.commit()

    def get_audio_by_category_id(self, category_id: str):
        sql = "SELECT file_id FROM audio_category WHERE category_id=%s"
        self.connection.reconnect(attempts=2)
        with self.connection.cursor() as cursor:
            cursor.execute(sql, (category_id,))
            result = cursor.fetchall()
            return result
