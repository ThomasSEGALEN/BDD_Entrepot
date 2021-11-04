# CRUD
# create, read, update, delete

import mysql.connector
import os
from employees import Employees
from warehouse import Warehouses
from products import Products

def format_text(liste):
    result = ""
    for i in liste:
        result += "\n"
        for j in i:
            result += str(j) + " | "

    return result

def clear_text():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)



cnx = mysql.connector.connect(host='localhost', database='mydb', user='root', password='')

while True:
    print("1 - employés")
    print("2 - produits")
    print("3 - entrepot")
    print("99 - quitter")
    choix = input("Que voulez vous ? : ")

    # Employees
    if choix == "1":
        employees_obj = Employees(cnx)
        while True:
            clear_text()
            print("1 - Voir les employés")
            print("2 - Ajouter un employé")
            print("3 - Supprimer un employé")
            print("4 - Modifier les données d'un employé")
            print("99 - retour")
            choix_emp = input("Que voulez-vous ? : ")

            # READ
            if choix_emp == "1":
                clear_text()
                warehouse_tmp = Warehouses(cnx)
                choix_ent = input("Voulez-vous choisir un entrepot en particulier ? (O/N): ")

                if choix_ent == "O" or choix_ent == "o":
                    print(warehouse_tmp.get_information())
                    choix_id = input("Lequel voulez-vous ? : ")
                    if choix_id in warehouse_tmp.get_id():
                        print(format_text(employees_obj.get_information_by_id(choix_id)))
                        quit = input("Entrer pour quitter")
                    else:
                        print("mauvais id")
                        quit = input("Entrer pour quitter")
                        break
                else:
                    print(format_text(employees_obj.get_information()))
                    quit = input("Entrer pour quitter")
                    break
            # CREATE
            elif choix_emp == "2":
                clear_text()
                lastname_emp = input("Lastname : ")
                firstname_emp = input("Firstname : ")
                age_emp = input("Age : ")
                jobsid_emp = input("jobs_id : ")
                civilityid_emp = input("civlity_id : ")
                warehouseid_emp = input("warehouse_id : ")
                employees_obj.create(lastname_emp, firstname_emp, age_emp, jobsid_emp, civilityid_emp, warehouseid_emp)
                print("Vous avez créé un employé")
                break
            # DELETE
            elif choix_emp == "3":
                clear_text()
                id_emp = input("Id de l'employé : ")
                employees_obj.delete(id_emp)
                print("Vous avez supprimé un employé")
                break
            # UPDATE
            elif choix_emp == "4":
                clear_text()
                champ_emp = input("Champ à modifier : ")
                valeur_emp = input("Valeur du champ : ")
                id_emp = input("Id de l'employé : ")
                employees_obj.modify(champ_emp, valeur_emp, id_emp)
                print("Vous avez modifié un employé")
                break
            elif choix_emp == "99":
                clear_text()
                break
    # Products
    elif choix == "2":
        product_obj = Products(cnx)
        while True:
            clear_text()
            print("1 - Voir les produits")
            print("2 - Ajouter un produit")
            print("3 - Supprimer un produit")
            print("4 - Modifier les données d'un produit")
            print("99 - retour")
            choix_prod = input("Que voulez-vous ? :")

            # READ
            if choix_prod == "1":
                clear_text()
                warehouse_tmp = Warehouses(cnx)
                choix_ent = input("Voulez-vous choisir un entrepot en particulier ? (O/N): ")

                if choix_ent == "O" or choix_ent == "o":
                    print(warehouse_tmp.get_information())
                    choix_id = input("Lequel voulez-vous ? : ")
                    if choix_id in warehouse_tmp.get_id():
                        print(format_text(product_obj.get_information_by_id(choix_id)))
                        quit = input("Entrer pour quitter")
                    else:
                        print("mauvais id")
                        quit = input("Entrer pour quitter")
                        break
                else:
                    print(format_text(product_obj.get_information()))
                    quit = input("Entrer pour quitter")
                    break
            # CREATE
            elif choix_prod == "2":
                clear_text()
                name_prod = input("Product name : ")
                description_prod = input("Description : ")
                price_prod = input("Price : ")
                quantity_prod = input("Quantity : ")
                weight_prod = input("Weight : ")
                height_prod = input("Height : ")
                category_id_prod = input("category_id : ")
                product_obj.create(name_prod, description_prod, price_prod, quantity_prod, weight_prod, height_prod, category_id_prod)
                print("Vous avez créer un produit")
                break
            # DELETE
            elif choix_prod == "3":
                clear_text()
                id_prod = input("Id du produit : ")
                product_obj.delete(id_prod)
                print("Vous avez supprimé un produit")
                break
            # UPDATE
            elif choix_prod == "4":
                clear_text()
                champ_prod = input("Champ à modifier : ")
                valeur_prod = input("Valeur du champ : ")
                id_prod = input("Id du produit : ")
                product_obj.modify(champ_prod, valeur_prod, id_prod)
                print("Vous avez modifié un produit")
                break
            elif choix_prod == "99":
                clear_text()
                break
    # Warehouse
    elif choix == "3":
        warehouse_obj = Warehouses(cnx)
        while True:
            clear_text()
            print("1 - Voir les entrepôts")
            print("2 - Ajouter un entrepôts")
            print("3 - Supprimer un entrepôts")
            print("4 - Modifier les données d'un entrepôts")
            print("99 - retour")
            choix_ware = input("Que voulez-vous ? : ")

            # READ
            if choix_ware == "1":
                clear_text()
                print(format_text(warehouse_obj.get_information()))
                break
            # CREATE
            elif choix_ware == "2":
                clear_text()
                name_ware = input("Nom : ")
                city_ware = input("Ville : ")
                quantity_product_max_ware = input("Nombre de produit max : ")
                warehouse_obj.create(name_ware, city_ware, quantity_product_max_ware)
                print("Vous avez créé un entrepôt")
                break
            # DELETE
            elif choix_ware == "3":
                clear_text()
                id_ware = input("Id de l'entrepôt : ")
                warehouse_obj.delete(id_ware)
                print("Vous avez supprimé un entrepôt")
                break
            # UPDATE
            elif choix_ware == "4":
                clear_text()
                champ_ware = input("Champ à modifier : ")
                valeur_ware = input("Valeur du champ : ")
                id_ware = input("Id de l'entrepôt : ")
                print("Vous avez modifié un entrepôt")
                warehouse_obj.modify(champ_ware, valeur_ware, id_ware)
                break
            elif choix_ware == "99":
                clear_text()
                break
    elif choix == "99":
        break