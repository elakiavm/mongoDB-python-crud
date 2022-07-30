'''
Created on 
    March 26, 202

Course work: 
    MongoDB CURD
    
@author: Elakia

Source:
    
'''

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

cluster = MongoClient('MONGO_URI')
db      = cluster['hollywood']
col     = db['movies']

def get_last_movie_id():

    last_movie_id  = col.find().sort([('movie_id', -1)]).limit(1)

    try:
        last_movie_id = last_movie_id[0]['movie_id']

    except:
        last_movie_id = 0

    return last_movie_id


@app.route("/", methods=['POST'])

def startpy():

    name = request.json['name']
    genre = request.json['genre']
    
    last_movie_id = get_last_movie_id()

    current_movie_id = last_movie_id + 1

    movie_dict = {

        "movie_id": current_movie_id,
        "name"    : name,
        "genre"   : genre

    }

    col.insert_one(movie_dict)

    return "success"

   
@app.route("/get", methods=['GET'])

def get_all_movie():

    movie = col.find()
    print(movie)

    movie_list = []

    for item in movie:

        movie_dict = {
            "movie_id": item['movie_id'],
            "name"    : item['name'],
            "genre"   : item['genre']

        }

        movie_list.append(movie_dict)

        print(item)
    
    return jsonify(movie_list)

@app.route("/get/<movie_id>", methods=['GET'])

def get_one_movie(movie_id):

    movie = col.find_one({'movie_id': int(movie_id)})
    print(movie)

   
    movie_dict = {
        "name" : movie['name'],
        "genre": movie['genre']

    }

    return movie_dict

@app.route("/edit/<movie_id>", methods=['POST'])

def edit_movie(movie_id):
    # movie = col.find_one({'movie_id': int(movie_id)})

    name  = request.json['name']
    genre = request.json['genre']

    movie_dict = {
    
        "name" : name,
        "genre": genre

    }

    col.update_many({'movie_id': int(movie_id)}, {'$set': movie_dict})
    
    return 'success'
    
@app.route("/delete/<movie_id>", methods=['DELETE'])

def delete_one_movie(movie_id):

    col.delete_many({'movie_id': int(movie_id)})

    return 'success'
if __name__ == "__main__":
    app.run()