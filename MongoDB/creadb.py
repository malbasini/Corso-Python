import pymongo
from pymongo import MongoClient
#eseguo la connessione a mongodb
client = MongoClient("localhost",27017)
#creo un database e lo chiamo testdb
db=client.testdb
#creo la collection persone
persone_coll = db.persone
persone_coll.create_index([("nome",pymongo.ASCENDING)])
persone_coll.create_index([("cognome",pymongo.ASCENDING)])
persone_coll.create_index([("computer",pymongo.ASCENDING)])
#creo un documento
p1 = {"Nome":"Mario","Cognome":"Rossi","Eta":30, "Computer":["Apple","Asus"]}
#inserisco il documento in mongodb
persone_coll.insert_one(p1)
#creo un documento
p2 = {"Nome":"Giuseppe","Cognome":"Verdi","Eta":45, "Computer":["Apple"]}
#inserisco il documento in mongodb
persone_coll.insert_one(p2)