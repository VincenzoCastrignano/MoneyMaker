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



# {
#     "user": {
#         "ID": 0,
#         "fname": "",
#         "name": "",
#         "age": 0,
#         "sex": 0,
#         "ps": "",
#         "pwd": "",
#         "activities": [
#             {
#                 "ID": "725967c8-afa0-462f-89ae-be0f8d1bb4a5",
#                 "name": "Tennis",
#                 "price": 500.0,
#                 "number": "15",
#                 "frequency": "jour"
#             }
#         ],
#         "budgets": [
#           {
#                 "price": 500.0,
#                 "date": "Juillet"
#           }
#         ]
#     }
# }