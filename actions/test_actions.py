import mysql.connector as mysql
conn= mysql.connect(user='root',password ='root',host='localhost',database='bot_data')
cursor = conn.cursor()

cursor.execute("show tables")
for i in cursor:
    print(i)