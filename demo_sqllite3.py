import csv
import sqlite3


data = []
with open("house.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        t = (float(row["loyer"]), float(row["surface"]))
        data.append(t)

with sqlite3.connect("house.db3") as conn:
    cursor = conn.cursor()
    sql = "delete from house"
    cursor.execute(sql)
    print(sql)
    for row in data:
        sql="insert into house(loyer,surface) values({},{})".format(row[0], row[1])
        print(sql)
        cursor.execute(sql)
    sql = "select * from house"
    print(sql)
    cursor.execute(sql)
    for row in cursor:
        print(row)




