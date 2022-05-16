from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Business")
        self.setFixedSize(QSize(400, 300))

        self.button = QPushButton("Clique ici!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("Good job bro.")
        self.button.setEnabled(False)

        # Also change the window title.
        self.setWindowTitle("Mon nouveau Business")

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

