
from pymongo import MongoClient
import gridfs

conn = MongoClient("localhost",27017)
db = conn.wangxuex
fs = gridfs.GridFS(db)
files = fs.find()
for i in files:
    with open(i.filename,'wb') as f:
        while True:
            data = i.read(64)
            if not data:
                break
            f.write(data)
conn.close()
