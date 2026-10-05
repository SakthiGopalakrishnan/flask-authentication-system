import sqlite3

conn = sqlite3.connect("users.db")

cur = conn.cursor()

cur.execute("DELETE FROM users")

conn.commit()
conn.close()

print("All users deleted")