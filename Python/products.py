import mysql.connector
from mysql.connector import errorcode

# config options
config = {
    'user': 'thomas',
    'password': 'thomas',
    'host': 'localhost',
    'database': 'mydb'
}

# connexion to the databse
try:
    connexion = mysql.connector.connect(**config)
    cursor = connexion.cursor()
    print("Connected to", config['database'])

# definition of the table
    args = "*"
    table = "products"

# insertion query
    insert_product =   ("INSERT INTO " + table + 
                    " (name, description, price, quantity, weight, height, category_id) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s)")
    print(insert_product)

# select query
    select_product =    ("SELECT " + args +
                        " FROM " + table)
    print(select_product)

# inputs of insert query
    name = input("Provide the\nname: ")
    description = input("description: ")
    price = input("price: ")
    quantity = input("quantity: ")
    weight = input("weight: ")
    height = input("height: ")
    category_id = input("category_id: ")
    data_product = (name, description, price, quantity, weight, height, category_id)
    print(data_product)

# execution
    cursor.execute(insert_product, data_product, select_product)
    product_no = cursor.lastrowid

# commit
    connexion.commit()

# error catch
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