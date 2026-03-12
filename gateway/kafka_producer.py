from kafka import KafkaProducer
import json
import time

producer = None

def get_producer():
    global producer

    if producer is None:
        while True:
            try:
                producer = KafkaProducer(
                    bootstrap_servers="kafka:9092",
                    value_serializer=lambda v: json.dumps(v).encode("utf-8")
                )
                print("Connected to Kafka")
                break
            except Exception:
                print("Waiting for Kafka...")
                time.sleep(5)

    return producer


def send_payment_event(data):
    p = get_producer()
    p.send("payments", data)