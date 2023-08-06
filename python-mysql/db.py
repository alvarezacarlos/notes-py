import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='USER_NAME',
    password='USER_PASSWORD',
    database='DB_NAME'
)

c = db.cursor()

c.execute("select * from prueba.Usuario")

res = c.fetchall()

print(res)
