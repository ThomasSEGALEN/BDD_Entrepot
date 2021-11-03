# CRUD
# create, read, update, delete

import mysql.connector
from Python.warehouse import Warehouses
import os
from employees import Employees
from products import Products

def format_texte(liste):
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
                print(format_texte(test.get_information()))
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
                id_emp = input("id de l'employé")
                test.delete(id_emp)
                print("Vous avez supprimé un employé")
                break
            elif choix_emp == "4":
                clear_text()
                champ_emp = input("Champ à modifier : ")
                valeur_emp = input("Valeur du champ : ")
                id_emp = input("Id de l'employé : ")
                test.modify(champ_emp, valeur_emp, id_emp)
                break
            elif choix_emp == "99":
                clear_text()
                break
    elif choix == "2":
        pass
        while True:
            print("1 - Voir les produits")
            print("Ajouter un produit")
            print("Supprimer un produit")
            print("Modifier les données d'un produit")
            print("99 - retour")
            choix_prod = input("Que voulez-vous ? :")

            if choix_prod == "1":
                print(format_text(test.get_information()))
                break
            elif choix_prod == "2":
                """name, description, price, quantity, weight, height, category_id"""
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
                id_prod = input("id du produit")
                test.delete(id_prod)
                print("Vous avez supprimé un produit")
                break
            elif choix_prod == "4":
                id_prod = input("Id du produit : ")
                champ_prod = input("Champ à modifier : ")
                valeur_prod = input("Valeur du champ : ")
                test.modify(id_prod, champ_prod, valeur_prod)
                break
            elif choix_ware == "99":
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
                print(format_texte(test.get_information()))
                break
            elif choix_ware == "2":
                """name, city, quantity_product_max, slot_id"""
                name_ware = input("Lastname : ")
                city_ware = input("Age : ")
                quantity_product_max_ware = input("jobs_id : ")
                slot_id_ware = input("civlity_id : ")
                test.create(name_ware, city_ware, quantity_product_max_ware, slot_id_ware)
                print("Vous avez créé un entrepôt")
                break
            elif choix_ware == "3":
                id_ware = input("id de l'entrepôt")
                test.delete(id_ware)
                print("Vous avez supprimé un entrepôt")
                break
            elif choix_ware == "4":
                id_ware = input("Id de l'entrepôt : ")
                champ_ware = input("Champ à modifier : ")
                valeur_ware = input("Valeur du champ : ")
                test.modify(id_ware, champ_ware, valeur_ware)
                break
            elif choix_ware == "99":
                break
    elif choix == "99":
        break