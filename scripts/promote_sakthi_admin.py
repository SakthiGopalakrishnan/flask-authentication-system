import sqlite3

with sqlite3.connect("users.db") as conn:

    cur = conn.cursor()

    cur.execute("""
    UPDATE users
    SET role='admin'
    WHERE username='sakthi'
    """)

    conn.commit()

print("sakthi promoted")