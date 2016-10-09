from flask import Flask
from flask import request
from flask import jsonify
import sqlite3
app = Flask(__name__)

conn = sqlite3.connect('db.db')

@app.route("/")
def hello():
	return "executed"

def jsonify_get_images(lst):
	ret_list = list()
	for img,logo in lst:
		ret_list.append({"image": img, "logo": logo})
	print (ret_list)
	return ret_list

@app.route("/images",  methods=['POST', 'GET', 'PUT'])
def images():
	if request.method == 'GET':
		return get_images(request)
	elif request.method == 'PUT':
		return put_images(request)
	elif request.method == 'POST':
		return post_images(request)

def get_images(request):
	if request.args.get('image'):
		c = conn.cursor()
		c.execute('SELECT * FROM images where name=\'' + request.args.get('image') + '\'')
		return jsonify(jsonify_get_images(c.fetchall()))
	else: 
		c = conn.cursor()
		c.execute('SELECT * FROM images')
		return jsonify(jsonify_get_images(c.fetchall()))

def put_images(request):
	c = conn.cursor()
	image = request.json['image']
	link = request.json['link']
	c.execute("INSERT INTO images Values( '{image}', '{link}')".format(image=image, link=link))
	return get_images(request)

def post_images(request):
	image = request.json['image']
	return "FROM:"+ image.upper()
	



if __name__ == "__main__":
    app.run()