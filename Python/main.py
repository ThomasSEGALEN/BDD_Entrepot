# CRUD
# create, read, update, delete

import mysql.connector
from employees import Employees

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
                print(test.get_information())
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
    elif choix == "2":
        pass
    elif choix == "3":
        pass
    elif choix == "99":
        break