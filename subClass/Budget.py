import json
from fonction import *


# //////
#
# Méthode pour cette classe Budget :
# Elle possède juste un prix, et le mois auquel il réfère
# s'ajoute dans le json du user
# ensuite création d'une méthode pour tester si l'ensemble
# des prix des act est moins cher ou non, si c'est + cher
# alors ALERTE et impossible de rajouter d'autres act
# D'abord seulement pour les mois
#
# //////


class Budget:
    price: ''
    date: ''

    def __init__(self, price, date):
        self.price = price
        self.date = date

    def __str__(self):
        return 'price : ' + float(self.price) + ' €, date : ' + str(self.date)

    def get_Budget(self):
        return {
            'price': self.price,
            'date': self.date,
        }


def add_Bud():
    date = str(input(
        "Pour quel mois correspond ton budget ?\nJanv - Fevr - Mars - Avri - Mai - Juin - Juil - Aout - Sept - Octo - Nove - Dece\n"))
    i = 0
    while i != 1:
        if i == 2:
            print('\n\nAttention ! Tu as mal écrit le mois ! \n\n')
            date = str(input(
                "Pour quel mois correspond ton budget ?\nJanv - Fevr - Mars - Avri - Mai - Juin - Juil - Aout - Sept - Octo - Nove - Dece\n\n"))
        if date.lower() == 'janv':
            final_date = 'Janvier'
            i = 1
        elif date.lower() == 'fevr':
            final_date = 'Fevrier'
            i = 1
        elif date.lower() == 'mars':
            final_date = 'Mars'
            i = 1
        elif date.lower() == 'avril':
            final_date = 'Avril'
            i = 1
        elif date.lower() == 'mai':
            final_date = 'Mai'
            i = 1
        elif date.lower() == 'juin':
            final_date = 'Juin'
            i = 1
        elif date.lower() == 'juil':
            final_date = 'Juillet'
            i = 1
        elif date.lower() == 'août' or date.lower() == 'aout':
            final_date = 'Aout'
            i = 1
        elif date.lower() == 'sept':
            final_date = 'Septembre'
            i = 1
        elif date.lower() == 'octo':
            final_date = 'Octobre'
            i = 1
        elif date.lower() == 'nove':
            final_date = 'Novembre'
            i = 1
        elif date.lower() == 'dece':
            final_date = 'Decembre'
            i = 1
        else:
            i = 2
    price = float(input("De combien est ton budget ?\n"))
    print("\nTrès bien ! Pour résumer tu as sauvegardé ceci :\n", price, "€ Pour le mois --> ", final_date, '\n')
    temp_ja = Budget(price, final_date)
    ja = temp_ja.get_Budget()
    print(ja)
    edit_json1("budgets", ja)
    return ja


def del_Bud():
    taille = print_Bud()
    a = int(input("\nQuelle activité veux-tu supprimer ?\n"))
    maxi = len(taille)
    cpt = 0
    while cpt != 1:
        if a < 0 | a > maxi:
            print("Met un bon budget")
            a = int(input("\nQuelle activité veux-tu supprimer ?\n"))
        else:
            print("parfait")
            cpt = 1


def print_Bud(data=data_json1()):
    a = data
    i = 0
    liste = []
    print("Voici une petite liste de tes budgets :\n")
    for b in a["user"]["budgets"]:
        print("Budget ", i + 1, ":", b['price'], "€ pour le mois de -->",
              b['date'])
        i = i + 1
        liste.append(b)
    # vaz: int = liste.__sizeof__()
    return liste  # [{'price': 0.5, 'date': 'Fevrier'}, {'price': 500.0, 'date': 'Decembre'}]
