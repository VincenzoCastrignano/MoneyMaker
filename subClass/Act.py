import json
import uuid


class Act:
    ID: ''
    name: ''
    price: ''
    number: ''
    frequency: ''

    def __init__(self, ID, name, price, number, frequency):
        self.ID = ID
        self.name = name
        self.price = price
        self.number = number
        self.frequency = frequency

    def __str__(self):
        return 'ID : ' + str(self.ID) + 'Name : ' + str(self.name) + ', price : ' + str(self.price) + ', number : ' + str(self.number) + ', fréquency : ' + str(self.frequency)

    def get_Act(self):
        return {
            'ID': self.ID,
            'name': self.name,
            'price': self.price,
            'number': self.number,
            'frequency': self.frequency,
        }

def add_Act():
    ID = str(uuid.uuid4())
    name = str(input("Quel est le nom de l'activité ?\n"))
    frequency_m = input("\nA quel type de fréquence veux-tu assigner à cette activité ? (J, S, M, A)\n")
    if frequency_m == "J":
        a = "jour"
    elif frequency_m == "S":
        a = "semaine"
    elif frequency_m == "M":
        a = "mois"
    elif frequency_m == "A":
        a = "an"
    frequency_time = str(input("\nCombien de fois fais-tu cette activité par " + a + " ?\n"))
    price = float(input("\nEt pour finir, maintenant combien coûte ton activité ?\n"))
    print("\nTrès bien ! Pour résumer tu as sauvegardé ceci :\n", name, " ", price, "€ ", frequency_time, "/", a)
    number = frequency_time
    frequency = a
    temp_ja = Act(ID, name, price, number, frequency)
    ja = temp_ja.get_Act()
    print(ja)
    edit_json1("activities", ja)
    return ja

def add_Act_bis():
    ID = str(uuid.uuid4())
    name = str(input("Quel est le nom de l'activité ?\n"))
    frequency_m = input("\nA quel type de fréquence veux-tu assigner à cette activité ? (J, S, M, A)\n")
    if frequency_m == "J":
        a = "jour"
    elif frequency_m == "S":
        a = "semaine"
    elif frequency_m == "M":
        a = "mois"
    elif frequency_m == "A":
        a = "an"
    frequency_time = str(input("\nCombien de fois fais-tu cette activité par " + a + " ?\n"))
    price = float(input("\nEt pour finir, maintenant combien coûte ton activité ?\n"))
    print("\nTrès bien ! Pour résumer tu as sauvegardé ceci :\n", name, " ", price, "€ ", frequency_time, "/", a)
    number = frequency_time
    frequency = a
    temp_ja = Act(ID, name, price, number, frequency)
    ja = temp_ja.get_Act()
    print(ja)
    edit_json1("activities", ja)
    return ja


# def print_Act(data):
#     a = data
#     print("Voici une petite liste de tes activités :\n")
#     for i in a["act"]:
#         print("Activité ", i, ", ", a["act"][i], "\n")


def data_json1(path='json/User.json'):
    with open(path, "r") as js:
        value = json.load(js)
    return value


def edit_json1(key, func, path='json/User.json'):
    dico = data_json1()
    temp_dico = dico["user"][key]
    temp_dico.append(func)
    dico["user"][key] = temp_dico
    with open(path, 'w') as js:
        json.dump(dico, js, indent=4)
    return dico
