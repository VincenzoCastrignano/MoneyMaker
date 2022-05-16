# from subClass.App import *
from subClass.User import Create_User
from subClass.User import *
from subClass.Budget import *
from fonction import *
from PyQt5.QtWidgets import QApplication, QWidget

# Only needed for access to command line arguments
import sys

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = QWidget()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()

if __name__ == '__main__':
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


# Continuer et finir les Act (créer, modif, supprm, list) (1h30)
# Commencer à gérer une intéraction fluide sans erreur (3-4h)

 # --> Initialiser un json complet avec activités (vide), et budget (vide) Fonction Create_User()
 # --> Créer la fonction Add_Act() pour ajouter des act au json
 # --> Créer la fonction Add_Budget() pour ajouter des budgets au json
 # --> Stocker toutes ces données dans des variables locales et non au json