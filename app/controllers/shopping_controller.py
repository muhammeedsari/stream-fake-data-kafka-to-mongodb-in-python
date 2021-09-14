from app.models.shopping_model import ShoppingModel
from app.business.shopping_manager import ShoppingManager
from app.helpers.kafka import Kafka
import simplejson as json


class ShoppingController:
    def __init__(self):
        self.shopping_manager = ShoppingManager()

    def create_shopping(self):
        kafka = Kafka()
        consumer = kafka.create_consumer(topic="shopping")

        while True:
            msg = consumer.poll()

            if msg is None:
                continue
            if msg.error():
                print("Consumer error: {}".format(msg.error()))
                continue
            
        
            json_data = json.loads(msg.value().decode('utf-8'))
            
            print(json_data)
            shopping_obj = ShoppingModel(**json_data)
           
            self.shopping_manager.create_shopping(shopping_obj)