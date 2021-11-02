import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="test",
    password="test",
    database="mydb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM warehouses")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)