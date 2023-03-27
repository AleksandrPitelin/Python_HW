import sqlite3

db = sqlite3.connect("/Users/AleksandrPitelin/PythonProject/PythonProject/HomeWork_21/HW21.sqlite")
c = db.cursor()


c.execute(""" CREATE TABLE IF NOT EXISTS users (
    id integer PRIMARY KEY AUTOINCREMENT,
    first_name text,
    last_name text,
    age integer
)
""")
#
c.execute("SELECT * FROM users WHERE age > 30;")
rows = c.fetchall()
for row in rows:
    print(row)

#--------------------------#


c.execute("SELECT COUNT(*) FROM users WHERE age > 30;")
count = c.fetchone()[0]
print(count)


#---------------------------#



c.execute("SELECT age, COUNT(*) AS users FROM users GROUP BY age ORDER BY age;")
rows = c.fetchall()
for row in rows:
    print(row)

#---------------------------#

c.execute("SELECT age, COUNT(*) AS users FROM users GROUP BY age ORDER BY users DESC,age ASC;")
rows = c.fetchall()
for row in rows:
    print(row)




db.commit()
db.close()


