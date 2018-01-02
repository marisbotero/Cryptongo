import pymongo
from flask import Flask, jsonify, request

def get_db_connection(uri):
    client = pymongo.MongoClient(uri)
    return  client.cryptongo

app = Flask(__name__)
db_connection = get_db_connection('mongodb://localhost:27017')

def get_documents():
	params ={}
	name = int(request.args.get('name',''))
	limit = int(request.args.get('limit', 0))
	if name:
		params.udpate({'name':name})
	cursor=db_connection.tickers.find(
		params,{'_id':0,'ticker_hash':0}).limit(limit)
	return list(cursor)

def get_top20():
	pass

def remove_currency():
	pass
