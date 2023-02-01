import sqlite3


class Engineer:
    def __init__(self, name, age, profession, salary):
        self.name = name
        self.age = age
        self.profession = profession
        self.salary = salary


engineer1 = Engineer("joh", 25, "Software Engineer", 5000)
engineer2 = Engineer("Jack", 33, "Cloud Engineer", 25000)
engineer3 = Engineer("jenny", 55, "Backend Engineer", 54000)
engineer4 = Engineer("Tim", 44, "Machine Learning Engineer", 565000)

# connect to a database
conn = sqlite3.connect("engineers.db")

# creating a cursor for executing sql queries
cur = conn.cursor()


# create a table
def creating_table():
    try:
        cur.execute("""
            
            CREATE TABLE engineers(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                profession TEXT NOT NULL,
                salary INTEGER NOT NULL
            )
        
        """)

        cur.execute("INSERT INTO engineers(name, age, profession, salary) VALUES(?, ?, ?, ?)",
                    (engineer1.name, engineer1.age, engineer1.profession, engineer1.salary))
        cur.execute("INSERT INTO engineers(name, age, profession, salary) VALUES(?, ?, ?, ?)",
                    (engineer2.name, engineer2.age, engineer2.profession, engineer2.salary))
        cur.execute("INSERT INTO engineers(name, age, profession, salary) VALUES(?, ?, ?, ?)",
                    (engineer3.name, engineer3.age, engineer3.profession, engineer3.salary))
        cur.execute("INSERT INTO engineers(name, age, profession, salary) VALUES(?, ?, ?, ?)",
                    (engineer4.name, engineer4.age, engineer4.profession, engineer4.salary))
        conn.commit()
        print("The table was created and added records successfully!")

    except:
        print("An error occurred!")

    conn.close()
