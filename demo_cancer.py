import pandas as pd
import numpy as np
import sklearn.preprocessing as pp
import sklearn.model_selection as ms
import sklearn.ensemble as rf
from sklearn.tree import export_graphviz
import matplotlib.pyplot as plt
import pickle
import pymongo

# DataMart = Mongo
# Mes données sont structurées
# Accès à la collection cancer dans Mongo
with pymongo.MongoClient('localhost', 27017) as client:
    db = client.local
    rows = db.cancer.find()

    # Conversion en DataFrame Pandas
    dataframe = pd.DataFrame(list(rows))

# Sklearn
# Label
y = dataframe.diagnosis
# DataSet
x = dataframe.drop(["diagnosis", "id", "_id"], axis=1)

np.random.seed(0)
xtrain, xtest, ytrain, ytest = ms.train_test_split(x, y, train_size=0.8, test_size=0.2)

scaler = pp.StandardScaler()
scaler.fit(x)
xtrain = scaler.transform(xtrain)
xtest = scaler.transform(xtest)

# RandomForest
model = rf.RandomForestClassifier()

# Apprentissage
model.fit(xtrain, ytrain)

# Predit
ypredicted = model.predict(xtest)

# Save
with open("data/cancer/rf.pickle", "wb") as f:
    pickle.dump(model, f)

# Score = Accuracy = NbGood/NbTotal
score = model.score(xtest, ytest)
print(f"Score: {score:.2f}")

# Reverse engineering
export_graphviz(model.estimators_[0], out_file="data/cancer/tree.dot", feature_names=x.columns, class_names=["0", "1"])

print(model.feature_importances_)
plt.bar(x.columns, model.feature_importances_)
plt.xticks(rotation=45)
plt.show()
