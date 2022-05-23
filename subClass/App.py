from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
from random import choice
from random import randint
import sys

window_titles = [
    "Base",
    "Connexion",
    "Inscription",
    "Ajout Utilisateur",
    "Accueil",
    'Erreur'
]


class Inscription(QWidget):
    def __init__(self):
        super().__init__()
        form = QVBoxLayout()
        self.form_txt = QLabel("Inscription !")
        font = self.form_txt.font()
        font.setPointSize(30)
        self.form_txt.setFont(font)

        self.setWindowIcon(QtGui.QIcon('icon/money.png'))
        self.setWindowTitle(window_titles[2])
        self.setFixedSize(QSize(250, 350))
        form.addWidget(self.form_txt)
        self.setLayout(form)

        form_name = QLineEdit()
        form_name.setPlaceholderText("Prénom...")
        form.addWidget(form_name)
        form_f_name = QLineEdit()
        form_f_name.setPlaceholderText("Nom de famille...")
        form.addWidget(form_f_name)
        form_age = QSpinBox()
        form.addWidget(form_age)
        form_sex_2 = QComboBox()
        form_sex_2.addItem('A choisir')
        form_sex_2.addItem('Homme')
        form_sex_2.addItem('Femme')

        form.addWidget(form_sex_2)
        form_pseudo = QLineEdit()
        form_pseudo.setPlaceholderText("Pseudo...")
        form.addWidget(form_pseudo)
        form_pwd = QLineEdit()
        form_pwd.setPlaceholderText("Mot de passe...")
        form.addWidget(form_pwd)




        button1 = QPushButton("Annuler")
        button1.clicked.connect(self.button_clicked)
        # form.addWidget(button1)

        button2 = QPushButton("Valider")
        button2.clicked.connect(self.button_clicked)
        # form.addWidget(button2)

        form.addWidget(button1)
        form.addWidget(button2)
        self.setLayout(form)


    def button_clicked(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Sécurité")
        dlg.setText("Êtes-vous sûr ?")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()
        if button == QMessageBox.Yes:
            self.close()
        else:
            print("non")


class Connexion(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Pour te connecter, il te suffit de rentrer ton ps et mdp !")
        self.setWindowIcon(QtGui.QIcon('icon/money.png'))
        self.setWindowTitle(window_titles[1])
        self.setFixedSize(QSize(600, 750))
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('icon/money.png'))
        self.setWindowTitle("Business")
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
        self.addToolBar(toolbar)

        button_action = QAction(QIcon("icon/money.png"), "&Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon("icon/money.png"), "Your &button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()

        file_menu = menu.addMenu("&Option")
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action2)

    def toggle_w(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()

    def onMyToolBarButtonClick(self, s):
        print("click", s)
        # self.button = QPushButton("Clique ici!")
        # self.button.clicked.connect(self.the_button_was_clicked)
        # self.windowTitleChanged.connect(self.the_window_title_changed)
        # self.setCentralWidget(self.button)

        # def Clique(self, e):
        #     if e.button() == Qt.LeftButton:
        #         self.label.setText("Clique Gauche")
        #     elif e.button() == Qt.MiddleButton:
        #         self.label.setText("Clique Millieu")
        #     elif e.button() == Qt.RightButton:
        #         self.label.setText("Clique Droit")
        #
        # def mousePressEvent(self, e):
        #     self.label.setText("mousePressEvent")
        #
        # def mouseReleaseEvent(self, e):
        #     self.label.setText("mouseReleaseEvent")
        #
        # def mouseDoubleClickEvent(self, e):
        #     self.label.setText("mouseDoubleClickEvent")

        # layout = QVBoxLayout()
        # layout.addWidget(self.input)
        # layout.addWidget(self.label)
        #
        # container = QWidget()
        # container.setLayout(layout)

        # layout = QVBoxLayout()
        # widgets = [
        #     QCheckBox,
        #     QComboBox,
        #     QDateEdit,
        #     QDateTimeEdit,
        #     QDoubleSpinBox,
        #     QFontComboBox,
        #     QLCDNumber,
        #     QLabel,
        #     QLineEdit,
        #     QProgressBar,
        #     QPushButton,
        #     QRadioButton,
        #     QSlider,
        #     QSpinBox,
        #     QTimeEdit,
        # ]
        #
        # for w in widgets:
        #     layout.addWidget(w())

        # widget = QLabel("Bienvenue")
        # font = widget.font()
        # font.setPointSize(30)
        # widget.setFont(font)
        # widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # self.setCentralWidget(widget)
        #
        # # self.test = QLabel("Connexion", self)
        # # font = self.test.font()
        # # font.setPointSize(40)
        # # self.test.setAlignment(Qt.AlignCenter)
        #
        # self.label_Inscription = QLabel("Inscription", self)
        # self.label_Inscription.setStyleSheet("border: 1px solid black;")
        # self.label_Inscription.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        #
        # self.label_Connexion = QLabel("Connexion", self)
        # self.label_Connexion.setStyleSheet("border: 1px solid black;")
        # self.label_Connexion.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

    def the_button_was_clicked(self):
        print("Clique !")
        new_window_title = choice(window_titles)
        print("Paramètre du titre : %s" % new_window_title)

        # Also change the window title.
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print("Paramètre de fenêtre switch : %s" % window_title)
        if window_title == 'Erreur':
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
