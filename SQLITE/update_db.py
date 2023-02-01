import sqlite3
from mydb import Engineer

engineer5 = Engineer("Mirshod", 22, "Developer", 232000)

# fetching all data from the database
conn = sqlite3.connect("engineers.db")
cur = conn.cursor()
cur.execute("INSERT INTO engineers(name, age, profession, salary) VALUES(?, ?, ?, ?)",
            (engineer5.name, engineer5.age, engineer5.profession, engineer5.salary))

conn.commit()


def updating_row():
    # before updating
    cur.execute("SELECT * FROM engineers")
    my_data = cur.fetchall()
    print("Before updating row", my_data)

    # updating row
    update = "UPDATE engineers SET profession = 'Python Engineer', name = 'Patrick' WHERE name = 'Mirshod'"
    cur.execute(update)
    conn.commit()

    # after updating
    cur.execute("SELECT * FROM engineers")
    my_data = cur.fetchall()
    print("After updating row", my_data)


updating_row()