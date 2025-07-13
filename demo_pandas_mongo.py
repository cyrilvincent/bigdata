import pandas as pd
import matplotlib.pyplot as plt
import pymongo

with pymongo.MongoClient('localhost', 27017) as client:
    db = client.local
    rows = db.house.find()
    dataframe = pd.DataFrame(list(rows))
    print(dataframe.describe())

plt.scatter(dataframe['surface'], dataframe['loyer'])
plt.show()

