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

@app.route("/contact")
def contact():
	return render_template("contact.html")

@app.route("/apps",  methods=['POST', 'GET', 'PUT', 'DELETE'])
def apps():
	#return list of apps based on image name passed from 2nd screen
	if request.method == 'GET':
		return get_apps(request)
	if request.method == 'POST':
		return post_apps(request.args.get("os"), request.form.getlist('checked_app'))

@app.route("/commands",  methods=['POST', 'GET', 'PUT', 'DELETE'])
def commands():
	final_dockerfile = {}
	if request.method == 'POST':
		for i in request.form:
			if request.form[i] != '':
				final_dockerfile[i] = request.form[i]


	return post_commands(final_dockerfile)

		
if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)

