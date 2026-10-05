import sqlite3

with sqlite3.connect("users.db") as conn:

    cur = conn.cursor()

    cur.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    """)

    print(cur.fetchall())