# CRUD
# create, read, update, delete

import mysql.connector
from employees import Employees

a = mysql.connector.connect(host='localhost', database='mydb', user='root', password='')

test = Employees(a)

print(test.get_information())

# test.create("Dubuc", "Mathis", 19, 1, 1, 1)

# print(test.get_information())

# test.delete()

test.modify_age(40, 1)

print(test.get_information())

# print(a)