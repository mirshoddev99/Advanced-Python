import sqlite3

# fetching all data from the database
conn = sqlite3.connect("engineers.db")
cur = conn.cursor()


def remove_emp():

    # before deleting
    cur.execute("SELECT * FROM engineers")
    my_data = cur.fetchall()
    print("Before deleting row", my_data)

    # deleting row
    update = "DELETE FROM engineers WHERE name = 'Patrick'"
    cur.execute(update)
    conn.commit()

    # after deleting
    cur.execute("SELECT * FROM engineers")
    my_data = cur.fetchall()
    print("After deleting row", my_data)


remove_emp()