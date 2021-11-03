class Warehouses:
    def __init__(self, myDB):
        self.myDB = myDB
        self.cursor = self.myDB.cursor()
    
    def get_information(self):
        result = []
        query = "SELECT * FROM warehouses;"
        self.cursor.execute(query)

        for (id, name, city, quantity_product_max, slot_id) in self.cursor:
            result.append([id, name, city, quantity_product_max, slot_id])

        return result
    
    def create(self, name, city, quantity_product_max, slot_id):
        query = ("INSERT INTO warehouses(lastname, firstname, age, jobs_id, civility_id, warehouse_id) VALUES (%s, %s, %s, %s, %s, %s);")
        self.cursor.execute(query, (name, city, quantity_product_max, slot_id))
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