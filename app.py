from flask import Flask, jsonify
import json
import requests

app = Flask(__name__)

def getData(user):
    url='https://aerothon19.firebaseio.com/Users/'
    data=requests.get(url+'.json').json()
    return data

app.secret_key='secret'
@app.route('/<uname>', methods=['GET'])
def index(uname):
    uname+='/'
    data=getData(uname)
    return jsonify(data)

@app.route("/", methods=['POST','GET'])
def display():
    return jsonify({'main':"This is main page"})