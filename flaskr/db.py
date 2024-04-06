import sqlite3

DATABASE = 'db.sqlite3'
def create_books_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS books (title,price,arrival_day)")#テーブルが存在しないと作成
