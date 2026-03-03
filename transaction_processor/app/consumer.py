from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "payment_requests",
    bootstrap_servers="kafka:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)