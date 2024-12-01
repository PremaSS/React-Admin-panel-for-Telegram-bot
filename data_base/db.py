import os

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
