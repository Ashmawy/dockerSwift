from flask import Flask, render_template
from flask import request
from flask import jsonify
from flask import json
from backend import *

import sqlite3
app = Flask(__name__)



@app.route("/")
def home():
	return render_template("index.html")

@app.route("/images",  methods=['POST', 'GET', 'PUT', 'DELETE'])
def images():
	if request.method == 'GET':
		return get_images(request)
	elif request.method == 'PUT':
		return put_images(request)
	elif request.method == 'POST':
		return post_images(request)
	elif request.method== 'DELETE':
		return delete_images(request)
		
if __name__ == "__main__":
    app.run()

