
from app.controllers.shopping_controller import ShoppingController
from app.data_access.personDAL import PersonDal
from app.helpers.mongodbConnector import Connection

connection=Connection()
connection.connect_mongodb()


shopping_controller = ShoppingController()
shopping_controller.create_shopping()


