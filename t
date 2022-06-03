class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
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
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
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
        if window.isVisible():
            window.hide()
        else:
            window.show()

    def onMyToolBarButtonClick(self, s):
        print("click", s)

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


form = QVBoxLayout()
        self.form_txt = QLabel("Ecris ton pseudo Et ton mot de passe !")
        font = self.form_txt.font()
        font.setPointSize(20)
        self.form_txt.setFont(font)
        self.setWindowIcon(QtGui.QIcon('icon/money.png'))
        self.setWindowTitle(window_titles[1])
        self.setFixedSize(QSize(250, 350))
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