import sqlite3
db = sqlite3.connect("/Users/AleksandrPitelin/Downloads/book_store.sqlite")
c = db.cursor()
print(db)
c.fetchall()
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
c.execute("""CREATE TABLE IF NOT EXISTS purchases(
          id INTEGER,
          user_id INTEGER,
          book_id INTEGER,
          date INTEGER,
          FOREIGN KEY (user_id) references users(id),
          FOREIGN KEY (book_id) references books(id)
 )
 """)

c.execute("SELECT purchases.id, purchases.date, users.first_name, users.last_name FROM purchases INNER JOIN users ON purchases.user_id = users.id")
c.fetchall()
c.execute("SELECT users.id, users.first_name, users.last_name, books.title FROM users INNER JOIN purchases ON users.id = purchases.user_id INNER JOIN books ON purchases.book_id = books.id ORDER BY users.id")
c.fetchall()
c.execute("SELECT users.id, users.first_name, users.last_name, SUM(books.price) as total_purchases FROM users INNER JOIN purchases ON users.id = purchases.user_id INNER JOIN books ON purchases.book_id = books.id GROUP BY users.id")
c.fetchall()



db.commit()
db.close()