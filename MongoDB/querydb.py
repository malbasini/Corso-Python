import pymongo
from pymongo import MongoClient
#I connect to mongodb
client = MongoClient("localhost",27017)
#access to database called testdb
db=client.testdb
#create the people collection
persone_coll = db.persone
p=persone_coll.find_one()
persone = persone_coll.find({"Computer":"Asus"})
for p in persone:
    print(p) 
print('**************')
#Update operatore $set
result = persone_coll.update_one({"Nome":"Giuseppe"},{"$set":{"Eta":50}})
p=persone_coll.find_one({"Nome":"Giuseppe"})
print(p)
print('************************')
#$gt=Greater Than operatore $gt
persona = persone_coll.find_one({"Nome":{"$gt":"Giuseppe"}})
print(persona)