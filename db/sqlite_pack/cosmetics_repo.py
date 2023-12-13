from db.sqlite_pack._base_db_connector import BaseDbConnection


class CosmeticsRepo:
    def __init__(self, db_params):
        self._db = BaseDbConnection(db_params)
        self._table_name = 'COSMETICS'

    def get_the_last_row_id(self):
        res = self._db.cursor.execute(f"SELECT last_insert_rowid() FROM {self._table_name}")
        return res.fetchone()[0]

    def get_all(self):
        res = self._db.cursor.execute(f"SELECT * FROM {self._table_name}")
        return res.fetchall()

    def get_one_by_id(self, product_id: int):
        res = self._db.cursor.execute(f"SELECT * FROM {self._table_name} WHERE ProductID = {product_id}")
        emp = res.fetchone()
        return emp

    def insert_one(self,  name: str, product_type: str, price: float, manufacturer: str, availability: int):
        query_insert = f'''
                INSERT INTO {self._table_name} (ProductName, ProductType, Price, Manufacturer, InStock)
                VALUES ('{name}', '{product_type}', {price}, '{manufacturer}', {availability});
                '''
        self._db.cursor.execute(query_insert)
        self._db.conn.commit()

    def update_one_by_id(self, product_id: int, name: str, product_type: str, price: float, manufacturer: str, availability: int):
        query_update = f'''
                UPDATE {self._table_name}
                SET ProductName='{name}', ProductType='{product_type}', Price={price}, Manufacturer='{manufacturer}', InStock= {availability}
                WHERE ProductID={product_id};
                '''
        self._db.cursor.execute(query_update)
        self._db.conn.commit()

    def delete_one_by_id(self, product_id: int):
        query_delete = f'''
                DELETE FROM {self._table_name}
                WHERE ProductID = {product_id};
                '''
        self._db.cursor.execute(query_delete)
        self._db.conn.commit()

    def delete_last_row(self):
        query_delete = f'''
                DELETE FROM COSMETICS
                WHERE ProductID = (SELECT MAX(ProductID) FROM COSMETICS);
                '''
        self._db.cursor.execute(query_delete)
        self._db.conn.commit()

    def __del__(self):
        pass

