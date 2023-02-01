import sqlite3

# fetching all data from the database
conn = sqlite3.connect("engineers.db")
cur = conn.cursor()

cur.execute("SELECT * FROM engineers")
my_data = cur.fetchall()
for i, v in enumerate(my_data):
    print(f"{[v]}")
print()


cur.execute("SELECT name, profession FROM engineers WHERE name = 'Tim'")
result = cur.fetchone()
print(result)
print()
