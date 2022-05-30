from subClass.User import *
from subClass.Budget import *
from fonction import *
from subClass.App import *

import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
    # edit_json("ID", 15)
    # modif_User()
    # add_Act()
    # add_Bud()
    # print_Bud()
    # del_Bud()
    # print_Act()
    # Create_User()
    # data_json()
    # create_json({'ID': 6, 'fname': 'Castrignano', 'name': 'Vincenzo', 'age': 18, 'sex': 1, 'ps': 'Slayzen', 'pwd': 'pwd'})
    # start()

# Planning du cours :

# Régler le code erreur (ligne 109 fonction check) (Pas de temps)
# Créer fonction pour activer le boutton de l'inscription (45min)
# Créer une fonction pour la connexion (1h30)
