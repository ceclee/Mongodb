
from pymongo import MongoClient
import pymongo

conn = MongoClient('localhost',27017)
db = conn.powpow
my_set = db.gongrong
print(my_set)
# print(db)
# print(conn)
# my_set.insert([{"name":'gongd','age':78},{"name":'ninghao',"age":36}])
# my_set.save({'_id':1,"na11":9090})
# my_set.remove({"name":"liy"},multi=True)
cursor = my_set.find({"age":{"$gt":35}},{'_id':0})
# cursor = my_set.find()

# for i in cursor.sort([("age",1)]):
#     print(i)
# print(cursor.count())
# for i in cursor:
#     print(i)

# my_set.update({'name':"xufengkai"},{'$set':{'name':"alafate"}},upsert=True,multi=True)
# index = my_set.ensure_index([("name",1),("age",1)])
# print(index)
# my_set.drop_index()
for i in my_set.list_indexes():
    print(i)
