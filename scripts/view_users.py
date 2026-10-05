import sqlite3

conn=sqlite3.connect("users.db")
cur=conn.cursor()
cur.execute("SELECT * FROM users")
users=cur.fetchall()
for user in users:
    print(user)
conn.close()
