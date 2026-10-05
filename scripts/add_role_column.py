import sqlite3

with sqlite3.connect("users.db") as conn:

    cur=conn.cursor()

    cur.execute("""
    ALTER TABLE users
    ADD COLUMN role TEXT
    """)

print("Role column added")