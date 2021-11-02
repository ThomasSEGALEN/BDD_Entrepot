class Employees:
    def __init__(self, myDB):
        self.myDB = myDB
        self.cursor = self.myDB.cursor()

    def get_information(self):
        result = []
        query = "SELECT * FROM employees;"
        self.cursor.execute(query)

        for (id, lastname, firstname, age, jobs_id, civility_id, warehouse_id) in self.cursor:
            result.append([id, lastname, firstname, age, jobs_id, civility_id, warehouse_id])

        return result

    def create(self, lastname, firstname, age, jobs_id, civility_id, warehouse_id):
        query = ("INSERT INTO employees(lastname, firstname, age, jobs_id, civility_id, warehouse_id) VALUES (%s, %s, %s, %s, %s, %s);")
        self.cursor.execute(query, (lastname, firstname, age, jobs_id, civility_id, warehouse_id))
        self.myDB.commit()

    def delete(self, id):
        print(self.get_information())
        query = ("DELETE FROM employees WHERE id=%s;")
        self.cursor.execute(query, (id,))
        self.myDB.commit()

    def modify(self, champ, valeur, id):
        query = ("UPDATE employees SET " + champ + " = %s WHERE id = %s;")
        self.cursor.execute(query, (valeur, id))
        self.myDB.commit()
