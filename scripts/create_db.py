import sqlite3

conn=sqlite3.connect("users.db")
cur=conn.cursor()
cur.execute("""
CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
password TEXT)""")

conn.commit()
conn.close()
print("Database Created")