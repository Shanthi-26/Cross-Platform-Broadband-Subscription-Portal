from pymongo import MongoClient
from config import MONGO_URI, DATABASE_NAME
from bson.objectid import ObjectId

client = MongoClient(MONGO_URI)
db = client.get_database(DATABASE_NAME)

def get_platforms():
    return list(db.platforms.find())

def get_combos_for_platform(platform_name):
    return list(db.combos.find({"platform": platform_name}))

def add_subscription(user_email, combo):
    data = {
        "user_email": user_email,
        "platform": combo["platform"],
        "combo_name": combo["name"],
        "price": combo["price"],
        "validity_days": combo["validity_days"],
        "speed": combo.get("speed", None),
        "offer_description": combo.get("offer_description", None),
        "discount": combo.get("discount", 0),
        "status": "active"
    }
    return db.subscriptions.insert_one(data)

def get_user(email):
    return db.users.find_one({"email": email})

def create_user(user_data):
    return db.users.insert_one(user_data)

def get_user_subscriptions(user_email):
    return list(db.subscriptions.find({"user_email": user_email}))

def update_subscription_expiry(subscription_id, new_expiry_date):
    db.subscriptions.update_one(
        {"_id": ObjectId(subscription_id)},
        {"$set": {"expiry_date": new_expiry_date, "status": "active"}}
    )

def cancel_subscription(subscription_id):
    db.subscriptions.update_one(
        {"_id": ObjectId(subscription_id)},
        {"$set": {"status": "cancelled"}}
    )
