import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()


create_user = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_user)

create_items = "CREATE TABLE IF NOT EXISTS items(id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(create_items)

create_stores =  "CREATE TABLE IF NOT EXISTS stores(id INTEGER PRIMARY KEY, name text)"
cursor.execute(create_stores)

connection.commit()
connection.close()
