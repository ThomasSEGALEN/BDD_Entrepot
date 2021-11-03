# CRUD
# create, read, update, delete

import mysql.connector
from Python.warehouse import Warehouses
import os
from employees import Employees

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
        test = Warehouses(a)
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
    elif choix == "3":
        test = Employees(a)
        while True:
            print("1 - Voir les entrepôts")
            print("2 - Ajouter un entrepôts")
            print("3 - Supprimer un entrepôts")
            print("4 - Modifier les données d'un entrepôts")
            print("99 - retour")
            choix_emp = input("Que voulez-vous ? : ")

            if choix_emp == "1":
                print(format_texte(test.get_information()))
                break
            elif choix_emp == "2":
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
                id_emp = input("id de l'employé")
                test.delete(id_emp)
                print("Vous avez supprimé un employé")
                break
            elif choix_emp == "4":
                champ_emp = input("Champ à modifier : ")
                valeur_emp = input("Valeur du champ : ")
                id_emp = input("Id de l'employé : ")
                test.modify(champ_emp, valeur_emp, id_emp)
                break
            elif choix_emp == "99":
                break
    elif choix == "99":
        break