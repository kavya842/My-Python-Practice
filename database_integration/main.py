import sqlite3
connect = sqlite3.connect('MyDataBase.db')
print("Connected to database successfully")
cursor = connect.cursor()
cursor.execute("select * from employees")
columns = cursor.fetchone()
for columns in columns:
    print(columns)
connect.close()
