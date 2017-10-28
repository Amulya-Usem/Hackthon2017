from pymongo import MongoClient

def initiateDb():
	client = MongoClient()
	db = client.core
	return db