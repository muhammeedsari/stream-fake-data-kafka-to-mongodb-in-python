from re import T
from app.models.mongodb.shopping_mongodb_model import ShoppingMongodbModel
from app.data_access.base.baseDAL import BaseDal


class ShoppingDal(BaseDal[ShoppingMongodbModel[T]]):
    def __init__(self):
        super().__init__()