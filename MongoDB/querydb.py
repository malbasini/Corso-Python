import pymongo
from pymongo import MongoClient
#eseguo la connessione a mongodb
client = MongoClient("localhost",27017)
#accedo al database
db=client.testdb
#accedo alla collection persone
persone_coll = db.persone
p=persone_coll.find_one()
persone = persone_coll.find({"Computer":"Asus"})
for p in persone:
    print(p) 
print('**************')
result = persone_coll.update_one({"Nome":"Giuseppe"},{"$set":{"Eta":50}})
p=persone_coll.find_one({"Nome":"Giuseppe"})
print(p)
print('************************')
persona = persone_coll.find_one({"Nome":{"$gt":"Giuseppe"}})
print(persona)