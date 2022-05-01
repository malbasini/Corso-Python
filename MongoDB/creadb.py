import pymongo
from pymongo import MongoClient
#I connect to mongodb
client = MongoClient("localhost",27017)
#create a database and call it testdb
db=client.testdb
#create the people collection
persone_coll = db.persone
persone_coll.create_index([("nome",pymongo.ASCENDING)])
persone_coll.create_index([("cognome",pymongo.ASCENDING)])
persone_coll.create_index([("computer",pymongo.ASCENDING)])
#create one document
p1 = {"Nome":"Mario","Cognome":"Rossi","Eta":30, "Computer":["Apple","Asus"]}
#insert the document in mongodb
persone_coll.insert_one(p1)
#create the document
p2 = {"Nome":"Giuseppe","Cognome":"Verdi","Eta":45, "Computer":["Apple"]}
#insert the document in mongodb
persone_coll.insert_one(p2)