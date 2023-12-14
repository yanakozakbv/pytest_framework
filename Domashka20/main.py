from constants import ROOT_PATH
from utilities.sqlite_cm import Sqlite


def create_table():

    query_create = '''
        CREATE TABLE IF NOT EXISTS COSMETICS  
        (
            ProductID INTEGER PRIMARY KEY,
            ProductName TEXT,
            ProductType TEXT,
            Price REAL,
            Manufacturer TEXT,
            InStock INTEGER CHECK (InStock IN (0, 1))
        );
        '''
    c.executescript(query_create)


def clear_data():
    query = '''
        DELETE FROM COSMETICS;
        '''
    c.executescript(query)


def data_entry():
    query_insert = '''
        INSERT INTO COSMETICS (ProductName, ProductType, Price, Manufacturer, InStock)
        VALUES 
        ('Lipstick', 'Decorative', 200, 'MAC', '1'),
        ('Cleanser', 'Skincare', 150, 'Neutrogena', '0'),
        ('Moisturizer', 'Skincare', 120, 'Nivea', '1');
        '''
    c.executescript(query_insert)


def execute_select_query(sql_query):
    return c.execute(sql_query)


if __name__ == '__main__':
    with Sqlite(f'{ROOT_PATH}/db/test.db') as c:
        create_table()
        clear_data()
        data_entry()
        res = execute_select_query("SELECT * FROM COSMETICS")
        print(res.fetchall())
        rep = execute_select_query("SELECT last_insert_rowid() FROM COSMETICS")
        print(rep.fetchone()[0])
