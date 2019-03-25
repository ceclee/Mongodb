
from pymongo import MongoClient
import bson.binary

conn = MongoClient('localhost',27017)
db = conn.tupian
my_set = db.tupians
# file = './li.png'
# f = open(file,'rb')
# dic = dict(content=bson.binary.Binary(f.read()),filename='liyang.png')
# my_set.insert(dic)
data = my_set.find_one({'filename':'liyang.png'})

with open('aaaaa.png','wb') as f:
    f.write(data['content'])
conn.close()
