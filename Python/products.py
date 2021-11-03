import mysql.connector

# Database connection
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'mydb'
}
connection = mysql.connector.connect(**config)
cursor = connection.cursor()
print('Connected to', config['database'])


# SELECT QUERY
def select(args, table):
    query = ('SELECT ' + args + ' FROM ' + table)
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)
print('-- Select query --')
args = input('args: ')
table = input('table: ')
if args == '':
    args = '*'
if table == '':
    table = 'products'
select(args, table)


# INSERT QUERY
def insert():
    query = ('INSERT INTO products(name, description, price, quantity, weight, height, category_id) VALUES (%s, %s, %s, %s, %s, %s, %s)')
    name = input('name: ')
    description = input('description: ')
    price = input('price: ')
    quantity = input('quantity: ')
    weight = input('weight: ')
    height = input('height: ')
    category_id = input('category_id: ')
    data = (name, description, price, quantity, weight, height, category_id)
    cursor.execute(query, data)
    connection.commit()
print('-- Insert query --')
<<<<<<< HEAD
# insert()
=======
insert()
>>>>>>> f83884d8f4ddbddd73efed91bc949af8b765016a


# UPDATE QUERY
def update(table, column):
    query = ('UPDATE ' + table + ' SET ' + column + ' = %s WHERE id = %s')
    id = input('id: ')
    value = input('value: ')
    cursor.execute(query, (value, id))
    connection.commit()
print('-- Update query --')
table = input('table: ')
column = input('column: ')
if table == '':
    table = 'products'
<<<<<<< HEAD
# update(table, column)
=======
update(table, column)
>>>>>>> f83884d8f4ddbddd73efed91bc949af8b765016a


# DELETE QUERY
def delete(table, column):
    query = ('DELETE FROM ' + table + ' WHERE ' + column + '= %s')
    value = input('value: ')
    cursor.execute(query, (value,))
    connection.commit()
    print('Number of rows deleted:', cursor.rowcount)
print('-- Delete query --')
table = input('table: ')
column = input('column: ')
if table == '':
    table = 'products'
<<<<<<< HEAD
# delete(table, column)
=======
delete(table, column)
>>>>>>> f83884d8f4ddbddd73efed91bc949af8b765016a


cursor.close()
connection.close()