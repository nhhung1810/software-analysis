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
    producer.send('my_topic', value=json.dumps({"a": "b"}))

    @staticmethod
    def send(topic, message):
        print('Sending message to kafka')
        print(Producer.producer)
        Producer.producer.send(topic, b'message')
        print('Message sent')
