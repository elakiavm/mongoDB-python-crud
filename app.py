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

mongo = MongoClient(MONGO_URI)
database = mongo['data']
collection = database['student_info']
@app.route("/", methods=['POST'])

def startpy():

    

    details_dict = {
        "reg_no":312320,
        "name"  : "Nagulraj",
        "year"  : 2,
        "dept"  : "CSE"

    }

   
    collection.insert_one(details_dict)

    return "success"

   
@app.route("/get", methods=['GET'])

def get_all_details():

    student_details = collection.find()
    print(student_details)

    student_list = []

    for detail in student_details:

        student_dict = {
    
            "reg_no": detail['reg_no'],
            "name"  : detail['name'],
            "year"  : detail['year'],
            "dept"  : detail['dept']

        }

        student_list.append(student_dict)

        print(detail)
    
    return jsonify(student_list)

@app.route("/get/<reg_no>", methods=['GET'])

def get_one_detail(reg_no):

    student = collection.find_one({'reg_no': int(reg_no)})
    print(student)

   
    student_dict = {
        "name"  : student['name'],
        "reg_no": student['reg_no'],
        "year"  : student['year'],
        "dept"  : student['dept']

    }

    
    return student_dict

@app.route("/update/<reg_no>", methods=['POST'])

def update_details(reg_no):
    
    name = request.json['name']
    year = request.json['year']

    # name = "Nagulr"
    # year = 2

    student_dictionary = {

    
        "name": name,
        "year": year

    }

    collection.update_many({'reg_no': int(reg_no)}, {'$set': student_dictionary})
    
    return 'success'
    
@app.route("/delete/<reg_no>", methods=['POST'])

def delete_one_student(reg_no):

    collection.delete_many({'reg_no': int(reg_no)})

    return 'success'
if __name__ == "__main__":
    app.run()
    startpy()