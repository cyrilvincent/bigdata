import sqlite3
import pandas as pd
import sqlalchemy
import matplotlib.pyplot as plt

with sqlite3.connect("data/house/house.db3") as conn:
    cursor = conn.cursor()
    sql = "select * from house"
    print(sql)
    cursor.execute(sql)
    for row in cursor:
        print(row)

    dataframe = pd.read_sql(sql, conn)
    print(dataframe.describe())

plt.scatter(dataframe['surface'], dataframe['loyer'])
plt.show()








