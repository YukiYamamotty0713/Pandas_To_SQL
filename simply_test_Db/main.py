import sqlite3

dbname = 'TEST.db'
conn = sqlite3.connect(dbname)
# sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()

# personsというtableを作成してみる
# 大文字部はSQL文。小文字でも問題ない。
cur.execute('CREATE TABLE if not exists persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')
cur.execute('INSERT INTO persons (name) VALUES("A")')
cur.execute('INSERT INTO persons (name) VALUES("B")')
cur.execute('INSERT INTO persons (name) VALUES("C")')
cur.execute('INSERT INTO persons (name) VALUES("D")')
cur.execute('INSERT INTO persons (name) VALUES("E")')
cur.execute('INSERT INTO persons (name) VALUES("F")')
cur.execute('update persons SET name = "Kitahama" where id = 7')
cur.execute('DELETE FROM persons where id = 10')

# データベースへコミット。これで変更が反映される。
conn.commit()
conn.close()
