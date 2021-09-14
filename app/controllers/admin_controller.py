from app.helpers.kafka import Kafka

class AdminController:

    def create_topic(self):
        kafka = Kafka()
        kafka.create_topics(topic="shopping", num_partitions=10)
        kafka.list_topics()
       
       