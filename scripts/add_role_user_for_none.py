import sqlite3

with sqlite3.connect("users.db") as conn:

    cur = conn.cursor()

    cur.execute("""
    UPDATE users
    SET role='user'
    WHERE role IS NULL
    """)

    conn.commit()

print("Roles updated")