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



a = mysql.connector.connect(host='localhost', database='mydb', user='root', password='')

while True:
    print("1 - employés")
    print("2 - produits")
    print("3 - entrepot")
    print("99 - quitter")
    choix = input("Que voulez vous ? : ")

    if choix == "1":
        test = Employees(a)
        while True:
            print("1 - Voir les employés")
            print("2 - Ajouter un employé")
            print("3 - Supprimer un employé")
            print("4 - Modifier les données d'un employé")
            print("99 - retour")
            choix_emp = input("Que voulez-vous ? : ")

            if choix_emp == "1":
                clear_text()
                warehouse_tmp = Warehouses(a)
                choix_ent = input("Voulez-vous choisir un entrepot en particulier ? (O/N): ")

                if choix_ent == "O" or choix_ent == "o":
                    print(warehouse_tmp.get_information())
                    choix_id = input("Lequel voulez-vous ? : ")
                    if choix_id in warehouse_tmp.get_id():
                        print(format_text(test.get_information_by_id(choix_id)))
                    else:
                        print("mauvais id")
                        break
                else:
                    print(format_text(test.get_information()))
                    break
            elif choix_emp == "2":
                clear_text()
                lastname_emp = input("Lastname : ")
                firstname_emp = input("Firstname : ")
                age_emp = input("Age : ")
                jobsid_emp = input("jobs_id : ")
                civilityid_emp = input("civlity_id : ")
                warehouseid_emp = input("warehouse_id : ")
                test.create(lastname_emp, firstname_emp, age_emp, jobsid_emp, civilityid_emp, warehouseid_emp)
                print("Vous avez créé un employé")
                break
            elif choix_emp == "3":
                clear_text()
                id_emp = input("Id de l'employé : ")
                test.delete(id_emp)
                print("Vous avez supprimé un employé")
                break
            elif choix_emp == "4":
                clear_text()
                champ_emp = input("Champ à modifier : ")
                valeur_emp = input("Valeur du champ : ")
                id_emp = input("Id de l'employé : ")
                test.modify(champ_emp, valeur_emp, id_emp)
                print("Vous avez modifié un employé")
                break
            elif choix_emp == "99":
                clear_text()
                break
    elif choix == "2":
        test = Products(a)
        while True:
            print("1 - Voir les produits")
            print("2 - Ajouter un produit")
            print("3 - Supprimer un produit")
            print("4 - Modifier les données d'un produit")
            print("99 - retour")
            choix_prod = input("Que voulez-vous ? :")

            if choix_prod == "1":
                clear_text()
                warehouse_tmp = Warehouses(a)
                choix_ent = input("Voulez-vous choisir un entrepot en particulier ? (O/N): ")

                if choix_ent == "O" or choix_ent == "o":
                    print(warehouse_tmp.get_information())
                    choix_id = input("Lequel voulez-vous ? : ")
                    if choix_id in warehouse_tmp.get_id():
                        print(format_text(test.get_information_by_id(choix_id)))
                    else:
                        print("mauvais id")
                        break
                else:
                    print(format_text(test.get_information()))
                    break
            elif choix_prod == "2":
                clear_text()
                name_prod = input("Product name : ")
                description_prod = input("Description : ")
                price_prod = input("Price : ")
                quantity_prod = input("Quantity : ")
                weight_prod = input("Weight : ")
                height_prod = input("Height : ")
                category_id_prod = input("category_id : ")
                test.create(name_prod, description_prod, price_prod, quantity_prod, weight_prod, height_prod, category_id_prod)
                print("Vous avez créer un produit")
                break
            elif choix_prod == "3":
                clear_text()
                id_prod = input("Id du produit : ")
                test.delete(id_prod)
                print("Vous avez supprimé un produit")
                break
            elif choix_prod == "4":
                clear_text()
                champ_prod = input("Champ à modifier : ")
                valeur_prod = input("Valeur du champ : ")
                id_prod = input("Id du produit : ")
                test.modify(champ_prod, valeur_prod, id_prod)
                print("Vous avez modifié un produit")
                break
            elif choix_prod == "99":
                clear_text()
                break
    elif choix == "3":
        test = Warehouses(a)
        while True:
            print("1 - Voir les entrepôts")
            print("2 - Ajouter un entrepôts")
            print("3 - Supprimer un entrepôts")
            print("4 - Modifier les données d'un entrepôts")
            print("99 - retour")
            choix_ware = input("Que voulez-vous ? : ")

            if choix_ware == "1":
                clear_text()
                print(format_text(test.get_information()))
                break
            elif choix_ware == "2":
                clear_text()
                name_ware = input("Lastname : ")
                city_ware = input("Age : ")
                quantity_product_max_ware = input("jobs_id : ")
                slot_id_ware = input("civlity_id : ")
                test.create(name_ware, city_ware, quantity_product_max_ware, slot_id_ware)
                print("Vous avez créé un entrepôt")
                break
            elif choix_ware == "3":
                clear_text()
                id_ware = input("Id de l'entrepôt : ")
                test.delete(id_ware)
                print("Vous avez supprimé un entrepôt")
                break
            elif choix_ware == "4":
                clear_text()
                champ_ware = input("Champ à modifier : ")
                valeur_ware = input("Valeur du champ : ")
                id_ware = input("Id de l'entrepôt : ")
                print("Vous avez modifié un entrepôt")
                test.modify(champ_ware, valeur_ware, id_ware)
                break
            elif choix_ware == "99":
                clear_text()
                break
    elif choix == "99":
        break