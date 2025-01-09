import sqlite3


def initiate_db():
    conn = sqlite3.connect('database_m_14_4.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Products(
                 id INTEGER PRIMARY KEY,
                 title TEXT NOT NULL,
                 description TEXT,
                 price TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

    conn = sqlite3.connect('Users.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS Users(
                 id INTEGER PRIMARY KEY,
                 username TEXT NOT NULL, 
                 email TEXT NOT NULL,
                 age INTEGER NOT NULL,
                 balance INTEGER NOT NULL
    )
    ''')

    conn.commit()
    conn.close()




def get_all_products():
    conn = sqlite3.connect('database_m_14_4.db')
    c = conn.cursor()
    c.execute('SELECT * FROM Products')
    products = c.fetchall()
    conn.close()
    return products


def add_user(username, email, age):
    conn = sqlite3.connect('Users.db')
    c = conn.cursor()
    c.execute('INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)',
               (username, email, age, 1000))
    conn.commit()
    conn.close()


def is_included(username):
    conn = sqlite3.connect('Users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM Users WHERE username=?', (username,))
    row = c.fetchone()
    conn.close()
    if row is None:
        return False
    else:
        return True


# def content_db(title, description, price):
#     connection = sqlite3.connect('database_m_14_4.db')
#     cursor = connection.cursor()
#
#     con_db = cursor.execute('SELECT * FROM Products WHERE title=?', (title,))
#
#     if con_db.fetchone() is None:
#         cursor.execute(f'''
#     INSERT INTO Products (id, title, description, price) VALUES('{title}', '{description}', '{price}')
# ''')
#
#     connection.commit()
#     connection.close()
#
# content_db('Продукт 1', 'описание 1', 100)
# content_db('Продукт 2', 'описание 2', 200)
# content_db('Продукт 3', 'описание 3', 300)
# content_db('Продукт 4', 'описание 4', 400)


