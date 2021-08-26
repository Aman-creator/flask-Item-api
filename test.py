import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE users(id int, username char, password char)"
cursor.execute(create_table)

user = (1,'jose', 'asdf')
insert_query = 'INSERT INTO users VALUES(?,?,?)'
cursor.execute(insert_query,user)

users = [
    (2,'rolf', 'asdf'),
    (3,'aman', 'asdf')
]
cursor.executemany(insert_query,users)

select_query = 'select * from users'

for row in cursor.execute(select_query):
    print(row)

print('hello')
connection.commit()
connection.close()
