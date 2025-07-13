import pymongo
import json

with pymongo.MongoClient('localhost', 27017) as client:
    db=client.test # database created with MongoDbCompass
    collection = db.loyers
    print(collection)
    post={"id":1,"hello":"world"}
    id=collection.insert_one(post).inserted_id
    print(id)

    with open("house/encadrement_loyers.json") as f:
        s = f.read()
        js = json.loads(s)
        collection.insert_one(js)

    l = collection.find()
    print(l[1]["_id"])

    from bson.objectid import ObjectId
    l = collection.find({"_id":ObjectId("5a3454f724f3eb1ea0073cba")})
    print(l[0]["features"][0]["properties"][0])




