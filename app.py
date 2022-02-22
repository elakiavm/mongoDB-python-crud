from crypt import methods
from flask import Flask, request, jsonify
import pymongo
from pymongo import MongoClient 
from flask import Markup
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

	
MONGO_URI = os.environ.get('MONGO_URI')

cluster = MongoClient(MONGO_URI)
db = cluster['moives']