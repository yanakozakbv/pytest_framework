import sqlite3
from utilities.deco import singleton


@singleton
class BaseDbConnection:
    def __init__(self, db_params):
        self.__path = db_params
        self.conn = sqlite3.connect(database=self.__path)
        self.cursor = self.conn.cursor()

    def __del__(self):
        pass
        if self.cursor and self.conn:
            self.cursor.close()
            self.conn.close()
