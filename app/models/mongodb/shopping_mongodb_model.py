from mongoengine import *
from mongoengine.document import Document
from mongoengine.fields import *

class ShoppingMongodbModel(Document):
    name = StringField()
    gender = StringField()
    barcode = StringField()
    price = IntField()