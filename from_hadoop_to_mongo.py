import hdfs
import json
import pymongo
import csv
import io

client = hdfs.InsecureClient("http://localhost:50070")
with client.read("/house/house.csv") as f:
    reader = csv.DictReader(io.StringIO(f.read().decode('utf-8')))
    l = []
    for row in reader:
        json = {"loyer":float(row["loyer"]),"surface":float(row["surface"])}
        l.append(json)
    print(l)

with pymongo.MongoClient('localhost', 27017) as client:
    db = client.formation # database created with MongoDbCompass
    db.create_collection("house_from_hadoop")
    result = db.house.insert_many(l)
print(result.inserted_ids)





