from consumer import consumer
from database import SessionLocal
from models import Transaction

print("Transaction Processor Started...")

for message in consumer:
    data = message.value
    db = SessionLocal()

    transaction = db.query(Transaction).filter(
        Transaction.reference == data["reference"]
    ).first()

    if transaction:
        transaction.status = "success"
        db.commit()
        print(f"Processed transaction {transaction.reference}")

    db.close()