import sqlite3
from werkzeug.security import generate_password_hash

new_password = generate_password_hash("saki1234")

with sqlite3.connect("users.db") as conn:

    cur = conn.cursor()

    cur.execute("""
    UPDATE users
    SET password=?
    WHERE username='sakthi'
    """, (new_password,))

    conn.commit()

print("Password reset")