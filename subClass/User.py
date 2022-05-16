import json
import random
from fonction import *


class User:
    ID: ''
    fname: ''
    name: ''
    age: ''
    sex: ''
    ps: ''
    pwd: ''

    def __init__(self, ID, fname, name, age, sex, ps, pwd):
        self.ID = ID
        self.fname = fname
        self.name = name
        self.age = age
        self.sex = sex
        self.ps = ps
        self.pwd = pwd

    def __str__(self):
        return 'ID : ' + str(self.ID) + ', fname : ' + str(self.fname) + ', name : ' + str(
            self.name) + ', Age : ' + str(self.age) + ', Sex : ' + str(self.sex) + ', Ps : ' + str(
            self.ps) + ', Pwd : ' + str(self.pwd)

    def get_User(self):
        dictionary: dict = {
            'ID': self.ID,
            'fname': self.fname,
            'name': self.name,
            'age': self.age,
            'sex': self.sex,
            'ps': self.ps,
            'pwd': self.pwd,
        }
        return dictionary


def Create_User():
    ID = random.randint(0, 9)
    fname = str(input("Quel est ton Nom de Famille ?\n"))
    name = str(input("Quel est ton Prénom ?\n"))
    age = int(input("Quel est ton age ?\n"))
    b = True
    while b:
        sex = input("Quel est ton sexe ?\nH ou F\n")
        if sex == 'H':
            sex = 1
            b = False
        elif sex == 'F':
            sex = 0
            b = False
        else:
            print("Entre H pour homme ou F pour femme\n")
    ps = str(input("Quel est ton pseudonyme ?\n"))
    pwd = str(input("Quel est ton mot de passe ?\n"))
    temp_ja = User(ID, fname, name, age, sex, ps, pwd)
    ja = temp_ja.get_User()
    print(ja)
    create_json(ja)
    return ja


def Del_User(): # Pas fonctionnel
    create_json(0)
