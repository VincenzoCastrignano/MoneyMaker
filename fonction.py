import json
from subClass.User import *
from subClass.Act import add_Act


def create_json(func, path='json/User.json'):
    func['activities'] = list()
    func['budgets'] = list()
    dico = func
    with open(path, 'w') as js:
        json.dump({"user": dico}, js, indent=4)


def edit_json(key, func, path='json/User.json'):
    dico = data_json()
    dico["user"][key] = func
    with open(path, 'w') as js:
        json.dump(dico, js, indent=4)
    return dico


def data_json(path='json/User.json'):
    with open(path, "r") as js:
        value = json.load(js)
    return value


def start():
    a = input("----------------\nBonjour et bienvenue sur l'outil de gestion de budget !\n \nPossèdes-tu un compte ?\n")
    if a == "non":
        Create_User()
        print("\nBienvenue " + data_json()["user"]["name"] + "\n")
    else:
        ps = input("\nJ'aurais donc besoin de ton pseudo puis de ton mot de passe !\n\nPseudo : ")
        mdp = input("\nMot de passe : ")
        print("Bienvenue " + ps + " !\n")
    c = input("\nBon alors, Où veux-tu aller ?\n1) Profil...! \n2) Activités...!\n")
    if c == "1":
        inter_profil()
    if c == "2":
        add_Act()


def inter_profil():
    c = input("1) Modifier\n2) En cours...\n")
    if c == "1":
        print_User(modif_User())


def modif_User():
    b = data_json()
    a = input("\nPour commencer, que veux-tu modifier dans ton profil ?\n\n1) Nom\n2) Prénom\n3) Age\n4) Sexe\n5) "
              "Pseudo\n6) Mot de passe\n")
    if a == "1":
        d = "fname"
        print("Voici ton nom actuel : ", b["user"]["fname"])
        print("\n-----------------\n")
        c = input("Par quoi veux tu remplacer ton nom ?\n")
    if a == "2":
        d = "name"
        print("Voici ton prénom actuel : ", b["user"]["name"])
        print("\n-----------------\n")
        c = input("Par quoi veux tu remplacer ton prénom ?\n")
    if a == "3":
        d = "age"
        print("Voici ton âge actuel : ", b["user"]["age"])
        print("\n-----------------\n")
        c = input("Quel âge as-tu vraiment ?\n")
    if a == "4":
        d = "sex"
        if b["user"]["sex"] == 1:
            e = 0
            c = str(input("Tu es un homme, désires-tu changer ? o/n\n"))
            if c == "o":
                return edit_json(d, e)
            else:
                return edit_json(d, 1)
        else:
            e = 1
            c = str(input("Tu es une femme, désires-tu changer ? o/n\n"))
            if c == "o":
                return edit_json(d, e)
            else:
                return edit_json(d, 0)
    if a == "5":
        d = "ps"
        print("Voici ton pseudo actuel : ", b["user"]["ps"])
        print("\n-----------------\n")
        c = input("Par quoi veux tu remplacer ton pseudo ?\n")
    if a == "6":
        d = "pwd"
        print("Voici ton mot de passe actuel : ", b["user"]["pwd"])
        print("\n-----------------\n")
        c = input("Par quoi veux tu remplacer ton mot de passe ?\n")
    return edit_json(d, c)


def print_User(data):
    a = data
    print("\nVoici ton identité complète :")
    print("-----------------")
    print("Tu t'appelles ", a["user"]["name"], " ", a["user"]["fname"])
    print("Tu as ", a["user"]["age"], " ans")
    print("Ton pseudo est : ", a["user"]["ps"])
    if a["user"]["sex"] == 1:
        print("Tu es un Homme")
    else:
        print("Tu es une Femme")
    print("Ton mot de passe est : ", a["user"]["pwd"])
    print("-----------------\n")