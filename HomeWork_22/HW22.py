import sqlite3
db = sqlite3.connect("/Users/AleksandrPitelin/Downloads/book_store.sqlite")
c = db.cursor()
print(db)

c.execute("""CREATE TABLE IF NOT EXISTS users(
          id INTEGER PRIMARY KEY,
          first_name TEXT,
          last_name TEXT,
          age INTEGER
 )
 """),
c.execute("""CREATE TABLE IF NOT EXISTS publishing_house(
          id INTEGER PRIMARY KEY,
          name TEXT,
          rating INTEGER
 )
 """),
c.execute("""CREATE TABLE IF NOT EXISTS books(
          id INTEGER PRIMARY KEY,
          title TEXT,
          author TEXT,
          year INTEGER,
          price INTEGER,
          publishing_house_id INTEGER,
          FOREIGN KEY (publishing_house_id) references publishing_house(id)
 )
 """),
c.execute("""CREATE TABLE IF NOT EXISTS purchase(
          id INTEGER,
          user_id INTEGER,
          book_id INTEGER,
          date INTEGER,
          FOREIGN KEY (user_id) references users(id),
          FOREIGN KEY (book_id) references books(id)
 )
 """)


c.execute("SELECT purchase.id, purchase.date, users.first_name, users.last_name FROM purchase INNER JOIN users ON purchase.user_id = users.id")
res = c.fetchall()
for item in res:
    print(item)

c.execute("SELECT users.id, users.first_name, users.last_name, books.title FROM users INNER JOIN purchase ON users.id = purchase.user_id INNER JOIN books ON purchase.book_id = books.id ORDER BY users.id")
res = c.fetchall()
for item in res:
    print(item)
c.execute("SELECT users.id, users.first_name, users.last_name, SUM(books.price) as total_purchase FROM users INNER JOIN purchase ON users.id = purchase.user_id INNER JOIN books ON purchase.book_id = books.id GROUP BY users.id")
res = c.fetchall()
for item in res:
    print(item)



db.commit()
db.close()