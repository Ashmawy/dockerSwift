from flask import Flask, render_template
from flask import request
from flask import jsonify
from flask import json

import sqlite3
app = Flask(__name__)

conn = sqlite3.connect('db.db')

@app.route("/")
def hello():
	return render_template("index.html")

def jsonify_get_images(lst):
	ret_list = list()
	for img,logo in lst:
		ret_list.append({"image": img, "logo": logo})

	return ret_list

@app.route("/get-images")
def get_images():

	if request.args.get('image'):
		c = conn.cursor()
		c.execute('SELECT * FROM images where name=\'' + request.args.get('image') + '\'')
		return jsonify(jsonify_get_images(c.fetchall()))
	else: 
		c = conn.cursor()
		c.execute('SELECT * FROM images') 
		return render_template("images.html", data=jsonify_get_images(c.fetchall()))
		#return jsonify(jsonify_get_images(c.fetchall()))
		
if __name__ == "__main__":
    app.run()

