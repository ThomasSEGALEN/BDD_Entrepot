USE mydb;

-- TABLE "jobs"
ALTER TABLE jobs AUTO_INCREMENT = 1;
INSERT INTO jobs(name, salary) VALUES ("spécialiste informatique", 1500);
INSERT INTO jobs(name, salary) VALUES ("conducteur chariot", 1200);
INSERT INTO jobs(name, salary) VALUES ("spécialiste sport", 1500);
INSERT INTO jobs(name, salary) VALUES ("spécialiste jardin", 1500);
INSERT INTO jobs(name, salary) VALUES ("manager", 2000);

-- TABLE "category"
ALTER TABLE category AUTO_INCREMENT = 1;
INSERT INTO category(name, jobs_id) VALUES ("informatique", 1);
INSERT INTO category(name, jobs_id) VALUES ("sport", 2);
INSERT INTO category(name, jobs_id) VALUES ("jardin", 3);

-- TABLE "products"
ALTER TABLE products AUTO_INCREMENT = 1;
INSERT INTO products(name, description, price, quantity, weight, height, category_id) VALUES ("ordinateur", "un super ordi sous windows", 500, 10,  2, 30, 1);
INSERT INTO products(name, description, price, quantity, weight, height, category_id) VALUES ("telephone", "un téléphone génial pour passer des appels", 300, 10, 1, 20, 1);
INSERT INTO products(name, description, price, quantity, weight, height, category_id) VALUES ("pelle", "une pelle légendaire pour creuser", 30, 25, 1.5, 110, 3);
INSERT INTO products(name, description, price, quantity, weight, height, category_id) VALUES ("chaussure", "des chaussures pour bien marcher sur le sol", 100, 15, 0.5, 25, 2);

-- TABLE "slots"
ALTER TABLE slots AUTO_INCREMENT = 1;
INSERT INTO slots(name, disponible, warehouses_id) VALUES ("slot1", 1, 1);
INSERT INTO slots(name, disponible, warehouses_id) VALUES ("slot2", 1, 1);
INSERT INTO slots(name, disponible, warehouses_id) VALUES ("slot3", 1, 1);
INSERT INTO slots(name, disponible, warehouses_id) VALUES ("slot4", 1, 1);

-- TABLE "warehouses"
ALTER TABLE warehouses AUTO_INCREMENT = 1;
INSERT INTO warehouses(name, city, quantity_product_max) VALUES ("Le super Warehouse", "Angers", 50);

-- TABLE "civility"
ALTER TABLE civility AUTO_INCREMENT = 1;
INSERT INTO civility(name) VALUES ("male");
INSERT INTO civility(name) VALUES ("female");

-- TABLE "employees"
ALTER TABLE employees AUTO_INCREMENT = 1;
INSERT INTO employees(lastname, firstname, age, jobs_id, civility_id, warehouse_id) VALUES ("Martin", "Léo", 20, 1, 1, 1);
INSERT INTO employees(lastname, firstname, age, jobs_id, civility_id, warehouse_id) VALUES ("Dubois", "Lucas", 19, 1, 1, 1);
INSERT INTO employees(lastname, firstname, age, jobs_id, civility_id, warehouse_id) VALUES ("LeRoux", "Julie", 30, 2, 2, 1);
INSERT INTO employees(lastname, firstname, age, jobs_id, civility_id, warehouse_id) VALUES ("LeBlanc", "Simon", 20, 3, 1, 1);

-- TABLE "warehouses_has_products"

-- TABLE "height"
ALTER TABLE height AUTO_INCREMENT = 1;
INSERT INTO height(dimension) VALUES (10);
INSERT INTO height(dimension) VALUES (15);
INSERT INTO height(dimension) VALUES (20);
INSERT INTO height(dimension) VALUES (25);
INSERT INTO height(dimension) VALUES (30);

-- TABLE "products_has_slots"

-- TABLE "lane"
ALTER TABLE lane AUTO_INCREMENT = 1;
INSERT INTO lane(name, slots_id) VALUES ("lane1", 1);
INSERT INTO lane(name, slots_id) VALUES ("lane2", 1);

-- TABLE "level"
ALTER TABLE level AUTO_INCREMENT = 1;
INSERT INTO level(number, lane_id, height_id) VALUES (1, 1, 3);
INSERT INTO level(number, lane_id, height_id) VALUES (2, 1, 2);
INSERT INTO level(number, lane_id, height_id) VALUES (3, 1, 4);
INSERT INTO level(number, lane_id, height_id) VALUES (1, 2, 5);
INSERT INTO level(number, lane_id, height_id) VALUES (2, 2, 3);
INSERT INTO level(number, lane_id, height_id) VALUES (3, 2, 3);

