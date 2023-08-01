import pymongo

mongo_instance = pymongo.MongoClient("mongodb://localhost:27017/")

db = mongo_instance["my_db"] # In MongoDB, a database is not created until it gets content!
#MongoDB waits until you have created a collection (table), with at least one document (record) before it actually creates the database (and collection). Therefore,  you should create collection and create document before you check if the database exists!
