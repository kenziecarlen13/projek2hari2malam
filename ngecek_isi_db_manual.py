import sqlite3

connection = sqlite3.connect("user.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM user")
count=cursor.fetchall()
connection.close()

for i in count:
    print(i)