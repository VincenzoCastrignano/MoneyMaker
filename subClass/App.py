import time

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
from random import choice
from fonction import data_json
from subClass.Act import add_Act
from random import randint
import sys

from subClass.User import Create_User

window_titles = [
    "Base",
    "Connexion",
    "Inscription",
    "Ajout Utilisateur",
    "Accueil",
    'Erreur'
]


def loader(a=0):
    Home = Accueil()
    Fir = FirstW()
    match a:
        case 1:
            print("1")
            Home
        case _:
            print("default")
            Fir.Create_InsCo()


class Inscription(QWidget):
    def __init__(self):
        super().__init__()
        self.set_form()

    def clear_form(self):
        self.form_fname.clear()
        self.form_name.clear()
        self.form_age.clear()
        self.form_age.setValue(20)
        self.form_sex.clear()
        gender_list = ["A choisir", "Homme", "Femme", "Autre"]
        self.form_sex.addItems(gender_list)
        self.form_sex.setItemData(0, "A choisir")
        self.form_sex.setItemData(1, 1)
        self.form_sex.setItemData(2, 0)
        self.form_sex.setItemData(3, 2)
        self.form_pseudo.clear()
        self.form_pwd.clear()
        self.button2.setEnabled(False)

    def set_form(self):
        self.setWindowIcon(QtGui.QIcon('icon/money.png'))
        self.setWindowTitle(window_titles[2])
        self.setFixedSize(QSize(250, 350))
        form = QVBoxLayout()
        self.form_txt = QLabel("Inscription !")
        font = self.form_txt.font()
        font.setPointSize(30)
        self.form_txt.setFont(font)

        form.addWidget(self.form_txt)
        self.setLayout(form)

        self.form_fname = QLineEdit()
        self.form_fname.textChanged.connect(self.check)
        self.form_fname.setPlaceholderText("Nom de famille...")
        self.form_fname.setObjectName("fname")
        form.addWidget(self.form_fname)

        self.form_name = QLineEdit()
        self.form_name.textChanged.connect(self.check)
        self.form_name.setPlaceholderText("Prénom...")
        self.form_name.setObjectName("name")
        form.addWidget(self.form_name)

        self.form_age = QSpinBox(self)
        self.form_age.valueChanged.connect(self.check)

        self.form_age.setValue(0)
        self.form_age.setRange(0, 99)

        self.form_age.setObjectName('age')
        form.addWidget(self.form_age)

        gender_list = ["A choisir", "Homme", "Femme", "Autre"]
        self.form_sex = QComboBox(self)
        self.form_sex.addItems(gender_list)

        self.form_sex.setItemData(0, "A choisir")
        self.form_sex.setItemData(1, 1)
        self.form_sex.setItemData(2, 0)
        self.form_sex.setItemData(3, 2)

        self.form_sex.currentTextChanged.connect(self.check)
        self.form_sex.setObjectName('sex')
        form.addWidget(self.form_sex)

        self.form_pseudo = QLineEdit()
        self.form_pseudo.textChanged.connect(self.check)
        self.form_pseudo.setPlaceholderText("Pseudo...")
        self.form_pseudo.setObjectName('ps')
        form.addWidget(self.form_pseudo)

        self.form_pwd = QLineEdit()
        self.form_pwd.textChanged.connect(self.check)
        self.form_pwd.setEchoMode(QLineEdit.Password)
        self.form_pwd.setPlaceholderText("Mot de passe...")
        self.form_pwd.setObjectName('pwd')
        form.addWidget(self.form_pwd)

        self.button1 = QPushButton("Annuler")
        self.button1.clicked.connect(self.button_clicked)

        self.button2 = QPushButton("Valider")
        self.button2.setEnabled(False)
        self.button2.clicked.connect(self.recup_data)

        form.addWidget(self.button1)
        form.addWidget(self.button2)
        self.setLayout(form)

    def check(self):
        fname = self.form_fname.text()
        name = self.form_name.text()
        age = self.form_age.value()
        sex = self.form_sex.currentData()
        ps = self.form_pseudo.text()
        pwd = self.form_pwd.text()
        if fname != '' and name != '' and age >= 13 and sex != 'A choisir' and ps != '' and pwd != '':
            if pwd != '' or pwd != ' ':
                self.button2.setEnabled(True)
                self.button2.setCheckable(False)
        else:
            self.button2.setEnabled(False)

    def recup_data(self):
        self.w1 = Connexion()
        a = []
        fname = self.form_fname.text()
        name = self.form_name.text()
        age = self.form_age.value()
        sex = self.form_sex.currentText()
        ps = self.form_pseudo.text()
        pwd = self.form_pwd.text()
        a.append(fname)
        a.append(name)
        a.append(age)
        a.append(sex)
        a.append(ps)
        a.append(pwd)
        Create_User(a)
        self.clear_form()
        self.close()
        self.w1.show()

    def button_clicked(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Sécurité")
        dlg.setText("Êtes-vous sûr ?")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()
        if button == QMessageBox.Yes:
            self.clear_form()
            self.close()
            FirstW().Create_InsCo()


class Connexion(QWidget):
    def __init__(self):
        super().__init__()
        self.form_co()

    def form_co(self):
        form = QVBoxLayout()
        self.form_txt = QLabel("Ecris ton pseudo ")
        font = self.form_txt.font()
        font.setPointSize(20)
        self.form_txt.setFont(font)
        self.setWindowIcon(QtGui.QIcon('icon/money.png'))
        self.setWindowTitle(window_titles[1])
        self.setFixedSize(QSize(250, 300))
        form.addWidget(self.form_txt)
        self.setLayout(form)
        self.form_pseudo = QLineEdit()
        self.form_pseudo.textChanged.connect(self.check)
        self.form_pseudo.setPlaceholderText("Pseudo...")
        self.form_pseudo.setObjectName('ps')
        form.addWidget(self.form_pseudo)

        self.form_pwd = QLineEdit()
        self.form_pwd.textChanged.connect(self.check)
        self.form_pwd.setEchoMode(QLineEdit.Password)
        self.form_pwd.setPlaceholderText("Mot de passe...")
        self.form_pwd.setObjectName('pwd')
        form.addWidget(self.form_pwd)

        self.button1 = QPushButton("Annuler")
        self.button1.clicked.connect(self.button_clicked)

        self.button2 = QPushButton("Valider")
        self.button2.setEnabled(False)
        self.button2.clicked.connect(self.verif_co)

        form.addWidget(self.button1)
        form.addWidget(self.button2)
        self.setLayout(form)

    def check(self):
        ps = self.form_pseudo.text()
        pwd = self.form_pwd.text()
        if ps != '' and pwd != '':
            self.button2.setEnabled(True)

    def clear_form(self):
        self.form_pseudo.clear()
        self.form_pwd.clear()
        self.button2.setEnabled(False)

    def button_clicked(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Sécurité")
        dlg.setText("Êtes-vous sûr ?")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()
        if button == QMessageBox.Yes:
            self.clear_form()
            self.close()
            FirstW().Create_InsCo()

    def verif_co(self):
        self.w3 = Accueil()
        self.w2 = FirstW().Create_InsCo()
        a = data_json()
        js_ps = a["user"]["ps"]
        js_pwd = a["user"]["pwd"]
        ps = self.form_pseudo.text()
        pwd = self.form_pwd.text()
        if js_ps == ps and js_pwd == pwd:
            self.close()
            FirstW().close()
            loader(1)
        else:
            FirstW().close()
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Erreur")
            dlg.setIcon(QMessageBox.Critical)
            dlg.setText("Mot de passe erroné")
            dlg.setStandardButtons(QMessageBox.Ok)
            button = dlg.exec()
            if button == QMessageBox.Ok:
                a = self.form_pseudo.text()
                self.clear_form()
                self.form_pseudo.setText(a)


class Accueil(QWidget):
    def __init__(self):
        super().__init__()
        self.defaultW()

    def defaultW(self):
        self.show()
        self.setWindowIcon(QtGui.QIcon('icon/money.png'))
        self.setWindowTitle(window_titles[4])
        self.setFixedSize(QSize(400, 500))
        data = data_json()
        print("ce data : ", data)
        data_budget = data['user']['budgets']
        data_act = data['user']['activities']
        Budget = QHBoxLayout()
        if not data_budget:
            a = "Vous n'avez aucun Budget"
        else:
            i = 0
            liste = []
            for b in data_budget:
                i = i + 1
                liste.append(b)
            a = b['date'] # +"data['user']['budgets']['date']"
        self.button_bu = QPushButton(a)
        self.button_bu.setMinimumWidth(40)
        Budget.addWidget(self.button_bu)

        if not data_act:
            c = "Vous n'avez aucune activité"
        else:
            i = 0
            liste = []
            for b in data_act:
                i = i + 1
                liste.append(b)
            c = b['price'] # +"data['user']['budgets']['date']"
            print(b['price'])
        self.button2 = QPushButton("Ajouter une Activité")
        self.button2.setEnabled(True)
        self.button2.clicked.connect(self.add_act)
        Budget.addWidget(self.button2)
        self.button_act = QPushButton(str(c))
        Budget.addWidget(self.button_act)
        self.setLayout(Budget)

    def add_act(self):
        self.w1 = Act_W()


class Act_W(QWidget):
    def __init__(self):
        super(Act_W, self).__init__()
        self.show()
        self.setWindowTitle("test")

class FirstW(QMainWindow):
    def __init__(self):
        super().__init__()

    def Create_InsCo(self):
        self.show()
        self.setWindowIcon(QtGui.QIcon('icon/money.png'))
        self.setWindowTitle(window_titles[0])
        self.setFixedSize(QSize(400, 600))

        self.w1 = Inscription()
        self.w2 = Connexion()

        a = QVBoxLayout()
        button1 = QPushButton("Inscription")
        button1.clicked.connect(
            lambda checked: self.toggle_w(self.w1)
        )
        a.addWidget(button1)

        button2 = QPushButton("Connexion")
        button2.clicked.connect(
            lambda checked: self.toggle_w(self.w2)
        )
        a.addWidget(button2)

        w = QWidget()
        w.setLayout(a)
        self.setCentralWidget(w)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        # self.addToolBar(toolbar)

        button_action = QAction(QIcon("icon/money.png"), "&Profil", self)
        button_action.setStatusTip("This is your button")
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon("icon/money.png"), "&A suivre...", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()

        file_menu = menu.addMenu("&Raccourci")
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action2)

    def toggle_w(self, window):
        self.hide()
        window.show()

class App:
    N_User: 0

    def __init__(self, N_User):
        self.N_User = N_User

    def add_user(self):
        first_name = self.fname.get()
        name = self.surname.get()
        ps = self.ps.get()
        pwd = self.pwd.get()
        User = self.N_User
        User += 1
        return {
            'fname': first_name,
            'name': name,
            'ps': ps,
            'pwd': pwd,
        }

    def Limit_User(self, N_User):
        if N_User > 10:
            print("Trop de User !")
