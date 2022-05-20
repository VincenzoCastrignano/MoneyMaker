from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import choice
import sys

window_titles = [
    "Base",
    "Connexion",
    "Inscription",
    "Ajout Utilisateur",
    "Accueil",
    'Something went wrong'
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_time_clicked = 0

        self.setWindowTitle("Business")

        self.setFixedSize(QSize(400, 300))

        self.button = QPushButton("Clique ici!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clique !")
        new_window_title = choice(window_titles)
        print("Paramètre du titre : %s" % new_window_title)

        # Also change the window title.
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print("Paramètre de fenêtre switch : %s" % window_title)
        if window_title == 'Something went wrong':
            self.button.setDisabled(True)


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
        User + 1
        return {
            'fname': first_name,
            'name': name,
            'ps': ps,
            'pwd': pwd,
        }

    def Limit_User(self, N_User):
        if N_User > 10:
            print("Trop de User !")
