import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'thomas',
    'password': 'thomas',
    'host': 'localhost',
    'database': 'mydb'
}

str 

try:
    connexion = mysql.connector.connect(**config)
    cursor = connexion.cursor()

    print("Connected to", config['database'])

    add_product =   ("INSERT INTO products "
                    " (name, description, price, quantity, weight, height, category_id) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s)")
    print(add_product)

    name = input("Provide the\nname: ")
    description = input("description: ")
    price = input("price: ")
    quantity = input("quantity: ")
    weight = input("weight: ")
    height = input("height: ")
    category_id = input("category_id: ")

    data_product = (name, description, price, quantity, weight, height, category_id)

    print(data_product)

    cursor.execute(add_product, data_product)
    product_no = cursor.lastrowid

    connexion.commit()

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
    cursor.close()
    connexion.close()