class Warehouses:
    def __init__(self, myDB):
        self.myDB = myDB
        self.cursor = self.myDB.cursor()
    
    def get_information(self):
        result = []
        query = "SELECT * FROM warehouses;"
        self.cursor.execute(query)

        for (id, name, city, quantity_product_max) in self.cursor:
            result.append([id, name, city, quantity_product_max])

        return result

    def get_id(self):
        result = []
        query = ("SELECT id FROM warehouses;")
        self.cursor.execute(query)

        for (id) in self.cursor:
            result.append(list(id))

        return "".join(map(str, result))

    def get_columns_name(self):
        result = []
        query = ("SHOW COLUMNS FROM warehouses;")
        self.cursor.execute(query)

        for (fields) in self.cursor:
            result.append([fields[0]])

        return result

    
    def create(self, name, city, quantity_product_max):
        query = ("INSERT INTO warehouses(name, city, quantity_product_max) VALUES (%s, %s, %s, %s);")
        self.cursor.execute(query, (name, city, quantity_product_max))
        self.myDB.commit()

    def delete(self, id):
        print(self.get_information())
        query = ("DELETE FROM warehouses WHERE id=%s;")
        self.cursor.execute(query, (id,))
        self.myDB.commit()
    
    def modify(self, champ, valeur, id):
        query = ("UPDATE warehouses SET " + champ + " = %s WHERE id = %s;")
        self.cursor.execute(query, (valeur, id))
        self.myDB.commit()