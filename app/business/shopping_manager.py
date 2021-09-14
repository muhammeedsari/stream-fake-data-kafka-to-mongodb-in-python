from app.models.mongodb.shopping_mongodb_model import ShoppingMongodbModel
from app.models.shopping_model import ShoppingModel
from app.data_access.shoppingDAL import ShoppingDal


class ShoppingManager:
    def __init__(self):
        self.shoppigdal = ShoppingDal()

    def create_shopping(self, shopping_model:ShoppingModel):
        shopping_mongodb = ShoppingMongodbModel()
        shopping_mongodb.name = shopping_model.name
        shopping_mongodb.gender = shopping_model.gender
        shopping_mongodb.barcode = shopping_model.barcode
        shopping_mongodb.price = shopping_model.price       
        
        self.shoppigdal.add(mongodb_context=shopping_mongodb, tag_list=["Shopping"])