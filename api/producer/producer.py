from kafka import KafkaProducer
import json


class Producer:
    print('Connecting to kafka server')
    producer = None

    try:
        producer = KafkaProducer(bootstrap_servers='kafka:9092', api_version=(0, 10, 0), value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    except Exception as e:
        print(e)
    print('Connected to kafka server')

    @staticmethod
    def send(topic, message):
        print('Sending message to kafka')
        Producer.producer.send(topic, json.dumps(message))
        print('Message sent')
