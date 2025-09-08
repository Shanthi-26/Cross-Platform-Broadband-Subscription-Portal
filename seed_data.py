from pymongo import MongoClient
from config import MONGO_URI, DATABASE_NAME

client = MongoClient(MONGO_URI)
db = client.get_database(DATABASE_NAME)

def seed_data():
    platform = {"name": "HomeNet", "image_filename": "images.png"}
    db.platforms.delete_many({})
    db.platforms.insert_one(platform)

    plans = [
        {"platform": "HomeNet", "category": "Speed-Based Broadband Plans", "name": "Basic 100 Mbps", "price": 499, "validity_days": 30, "speed": 100, "discount": 0},
        {"platform": "HomeNet", "category": "Speed-Based Broadband Plans", "name": "Standard 300 Mbps", "price": 799, "validity_days": 30, "speed": 300, "discount": 5},
        {"platform": "HomeNet", "category": "Speed-Based Broadband Plans", "name": "Premium 500 Mbps", "price": 1199, "validity_days": 30, "speed": 500, "discount": 10},
        {"platform": "HomeNet", "category": "Prepaid Plans", "name": "15 Days Prepaid", "price": 299, "validity_days": 15, "speed": 100, "discount": 5, "offer_description": "Limited Data"},
        {"platform": "HomeNet", "category": "Multi-Month Bundles", "name": "3 Months Speed Bundle (300 Mbps)", "price": 2199, "validity_days": 90, "speed": 300, "discount": 10},
        {"platform": "HomeNet", "category": "Streaming Combos", "name": "Basic + Netflix Lite", "price": 799, "validity_days": 30, "speed": 100, "discount": 0, "offer_description": "1 month free Netflix"},
        {"platform": "HomeNet", "category": "Streaming Combos", "name": "Standard + Hotstar VIP", "price": 999, "validity_days": 30, "speed": 300, "discount": 5, "offer_description": "2 months free Hotstar"},
        {"platform": "HomeNet", "category": "Welcome Offer", "name": "Welcome Pack", "price": 399, "validity_days": 30, "speed": 100, "discount": 20, "offer_description": "20% discount + OTT free"},
    ]
    db.combos.delete_many({})
    db.combos.insert_many(plans)
    print("Seed data inserted")

if __name__ == "__main__":
    seed_data()
