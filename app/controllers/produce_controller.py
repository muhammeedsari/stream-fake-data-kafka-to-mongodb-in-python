from app.models.shopping_model import ShoppingModel
import simplejson as json
from app.helpers.kafka import Kafka
from faker import Faker
import random


class ProduceController:
    def __init__(self):
        self.fake = Faker()
        self.kafka = Kafka()
        
    

    def produce_shopping(self):
        gender = "Male"
        gender_boolean = self.fake.boolean()
        if gender_boolean == True:
            gender = "Female"
        
        
        shopping = ShoppingModel(name = self.fake.name(), gender = gender, 
        barcode = self.fake.ean(length=13), price = random.randint(25, 250))
        shopping_dict = shopping.__dict__
        jsonObj = json.dumps(shopping_dict)

        self.kafka.produce_message(
            topic = "shopping", 
            key = "test_key", 
            value = jsonObj)








