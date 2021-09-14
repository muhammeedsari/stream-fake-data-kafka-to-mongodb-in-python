from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka import Producer, Consumer




def delivery_report(err, msg):
        if err is not None:
            print('Message delivery failed: {}'.format(err))
        else:
            print('Message delivered to {} [{}] {}'.format(msg.topic(), msg.partition(), msg.value().decode('utf-8')))


class Kafka:
    
    def __init__(self):
        self.adminClient = AdminClient({'bootstrap.servers': '165.232.152.207:9092'})

    def create_topics(self, topic: str, num_partitions: int):
        new_topics = [NewTopic(topic=topic, num_partitions=num_partitions, replication_factor=1)]
        fs = self.adminClient.create_topics(new_topics)
        for topic, f in fs.items():
            try:
                f.result()
                print("Topic {} created".format(topic))
            except Exception as e:
                print("Failed to create topic {}: {}".format(topic, e))

    def list_topics(self):
        print(self.adminClient.list_topics().topics)

    def produce_message(self, topic: str, key, value):
        producer = Producer({'bootstrap.servers': '165.232.152.207:9092'})
        producer.poll(0)
    
        producer.produce(topic=topic, key=key, value=value, callback=delivery_report)
        producer.flush()

    def create_consumer(self, topic:str):
        consumer = Consumer({
        'bootstrap.servers': '165.232.152.207:9092',
        'group.id': 'raw-data',
        'auto.offset.reset': 'earliest'})

        consumer.subscribe([topic])
        return consumer


            

    

        
        
            
    