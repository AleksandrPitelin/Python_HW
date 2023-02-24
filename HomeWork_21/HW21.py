import sqlite3

db = sqlite3.connect("/Users/AleksandrPitelin/PythonProject/PythonProject/HomeWork_21/HW21.sqlite")
c = db.cursor()
# print(db)

c.execute(""" CREATE TABLE IF NOT EXISTS users (
    id integer PRIMARY KEY AUTOINCREMENT,
    first_name text,
    last_name text,
    age integer
)
""")

# c.execute("INSERT INTO users VALUES ")

# c.execute("SELECT age FROM users WHERE age<30")
# print(c.fetchall())
# c.execute("SELECT id,age FROM users WHERE age>30, id")
# c.execute("SELECT id,age FROM users WHERE age>30, id")



db.commit()
db.close()


