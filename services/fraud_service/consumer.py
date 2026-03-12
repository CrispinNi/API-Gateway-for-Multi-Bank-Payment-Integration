from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "payment-events",
    bootstrap_servers="kafka:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

for message in consumer:

    payment = message.value

    if payment["amount"] > 10000:
        print("High risk transaction:", payment)

    else:
        print("Transaction OK")
