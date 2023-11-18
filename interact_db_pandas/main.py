import sqlite3
import pandas as pd

dbname = 'TEST.db'
conn = sqlite3.connect(dbname)
# sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()


# personsというtableを作成してみる
# 大文字部はSQL文。小文字でも問題ない。
cur.execute('CREATE TABLE if not exists persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING, address STRING)')

data = [
    {"name": "Alice", "address": "123 Main St"},
    {"name": "Bob", "address": "456 Oak Ave"},
    {"name": "Charlie", "address": "789 Pine Ln"},
    {"name": "David", "address": "101 Elm Rd"},
    {"name": "Eve", "address": "202 Cedar Blvd"},
    {"name": "Frank", "address": "303 Maple Dr"},
    {"name": "Grace", "address": "404 Birch Ct"},
    {"name": "Harry", "address": "505 Willow Pl"},
    {"name": "Ivy", "address": "606 Spruce Ave"},
    {"name": "Jack", "address": "707 Sycamore St"}
]

data_df = pd.DataFrame(data)
data_df.to_sql('persons', con=conn, if_exists='append', index=False)

# データベースへコミット。これで変更が反映される。
conn.commit()
conn.close()
