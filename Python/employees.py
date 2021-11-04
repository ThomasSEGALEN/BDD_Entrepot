class Employees:
    def __init__(self, myDB):
        self.myDB = myDB
        self.cursor = self.myDB.cursor()

    def get_information(self):
        result = []
        query = ("SELECT employees.id, lastname, firstname, age, jobs.name AS jobs, civility.name AS civility, warehouses.name AS warehouses FROM employees INNER JOIN jobs ON jobs.id = employees.jobs_id INNER JOIN civility ON civility.id = employees.civility_id INNER JOIN warehouses ON warehouses.id = employees.warehouse_id;")
        self.cursor.execute(query)

        for (id, lastname, firstname, age, jobs_id, civility_id, warehouse_id) in self.cursor:
            result.append([id, lastname, firstname, age, jobs_id, civility_id, warehouse_id])

        return result

    # Récupérer les information en filtrant par l'id d'un warehouse
    def get_information_by_id(self, id):
        result = []
        query = ("SELECT employees.id, lastname, firstname, age, jobs.name AS jobs, civility.name AS civility, warehouses.name AS warehouses FROM employees INNER JOIN jobs ON jobs.id = employees.jobs_id INNER JOIN civility ON civility.id = employees.civility_id INNER JOIN warehouses ON warehouses.id = employees.warehouse_id WHERE warehouses.id = %s;")
        self.cursor.execute(query, (id,))

        for (id, lastname, firstname, age, jobs_id, civility_id, warehouse_id) in self.cursor:
            result.append([id, lastname, firstname, age, jobs_id, civility_id, warehouse_id])

        return result

    def get_columns_name(self):
        result = []
        query = ("SHOW COLUMNS FROM employees;")
        self.cursor.execute(query)

        for (fields) in self.cursor:
            result.append([fields[0]])

        return result

    def create(self, lastname, firstname, age, jobs_id, civility_id, warehouse_id):
        query = ("INSERT INTO employees(lastname, firstname, age, jobs_id, civility_id, warehouse_id) VALUES (%s, %s, %s, %s, %s, %s);")
        self.cursor.execute(query, (lastname, firstname, age, jobs_id, civility_id, warehouse_id))
        self.myDB.commit()

    def delete(self, id):
        query = ("DELETE FROM employees WHERE id=%s;")
        self.cursor.execute(query, (id,))
        self.myDB.commit()

    def modify(self, champ, valeur, id):
        query = ("UPDATE employees SET " + champ + " = %s WHERE id = %s;")
        self.cursor.execute(query, (valeur, id))
        self.myDB.commit()

