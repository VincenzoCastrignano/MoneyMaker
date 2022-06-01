from subClass.User import *
from subClass.Budget import *
from fonction import *
from subClass.App import *

import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    loader()

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

# Faire un schéma pour chaque interface (30-45min)
# Appliquer sur le code (45min-1h)
# Faire interface une fois connecté (1h)
# Appliquer les fonc pour ajouter act et Budget (30-45min)
# Créer fonction pour vérifier si le Budget est tjrs vérifié (?min)
