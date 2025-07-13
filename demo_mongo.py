import pymongo
from bson.objectid import ObjectId

with pymongo.MongoClient('localhost', 27017) as client:
    db = client["local"]
    print(db.list_collection_names())
    print(db.house)
    row = db.house.find_one()
    print(row)
    rows = db.house.find()
    for row in rows:
        print(row)
    result = db.house.find({"_id":ObjectId("6873906701d628fe8211d826")})
    print(f"Loyer: {result[0]["loyer"]}")
    results = db.house.find({"surface": {"$gt": 200}}).sort("surface")
    print(f">200: {list(results)}")

# Inserting
# house = {"loyer": 999, "surface":999}
# post_id = db.house.insert_one(house).inserted_id




