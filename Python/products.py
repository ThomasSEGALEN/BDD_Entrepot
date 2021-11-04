class Products:
    def __init__(self, myDB):
        self.myDB = myDB
        self.cursor = self.myDB.cursor()

    def get_information(self):
        result = []
        query = ("SELECT products.id, products.name AS products, description, price, quantity, weight, height, category.name AS category FROM products INNER JOIN category ON category.id = products.category_id;")
        self.cursor.execute(query)

        for (id, name, description, price, quantity, weight, height, category_id) in self.cursor:
            result.append([id, name, description, price, quantity, weight, height, category_id])

        return result

    # Récupérer les information en filtrant par l'id d'un warehouse
    def get_information_by_id(self, id):
        result = []
        query = ("SELECT products.id, products.name AS products, description, price, quantity, weight, height, category.name AS category FROM products INNER JOIN category ON category.id = products.category_id INNER JOIN warehouses_has_products ON warehouses_has_products.products_id = products.id INNER JOIN warehouses ON warehouses.id = warehouses_has_products.warehouse_id WHERE warehouses.id = %s;")
        self.cursor.execute(query, (id,))

        for (id, name, description, price, quantity, weight, height, category_name) in self.cursor:
            result.append([id, name, description, price, quantity, weight, height, category_name])

        return result

    def create(self, name, description, price, quantity, weight, height, category_id):
        query = ("INSERT INTO products(name, description, price, quantity, weight, height, category_id) VALUES (%s, %s, %s, %s, %s, %s, %s);")
        self.cursor.execute(query, (name, description, price, quantity, weight, height, category_id))
        self.myDB.commit()

    def delete(self, id):
        print(self.get_information())
        query = ("DELETE FROM products WHERE id=%s;")
        self.cursor.execute(query, (id,))
        self.myDB.commit()

    def modify(self, champ, valeur, id):
        query = ("UPDATE products SET " + champ + " = %s WHERE id = %s;")
        self.cursor.execute(query, (valeur, id))
        self.myDB.commit()
