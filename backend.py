from flask import Flask, render_template
from flask import request
from flask import jsonify
from flask import json
from dockerfile import Dockerfile
import sqlite3
conn = sqlite3.connect('db.db')

def jsonify_get_images(lst):
	ret_list = list()
	for img,logo in lst:
		ret_list.append({"image": img, "logo": logo})
	print (ret_list)
	return ret_list

def get_images(request):
	if request.args.get('image'):
		c = conn.cursor()
		c.execute('SELECT * FROM images where name=\'' + request.args.get('image') + '\'')
		return render_template("images.html", data=jsonify_get_images(c.fetchall()))
	else: 
		c = conn.cursor()
		c.execute('SELECT * FROM images') 
		return render_template("images.html", data=jsonify_get_images(c.fetchall()))

def put_images(request):
	c = conn.cursor()
	image = request.json['image']
	link = request.json['link']
	c.execute("INSERT INTO images Values( '{image}', '{link}')".format(image=image, link=link))
	return get_images(request)

def post_images(request):
	image = request.json['image']
	return "FROM:"+ image.upper()

def delete_images(request):
	c = conn.cursor()
	name = request.json['image']
	c.execute("DELETE FROM images where name='{name}'".format(name=name))
	return get_images(request)

def get_apps(request):
	c = conn.cursor()
	c.execute('SELECT app_name, link FROM install_cmds where os_name=\'' + request.args.get('os') + '\'')
	return render_template("apps.html", data=jsonify_get_images(c.fetchall()))

def post_apps(os_name, apps):
	
	apps = apps
	os_name = os_name
	d = Dockerfile(os_name)
	c = conn.cursor()

	for app in apps:
		c.execute('SELECT cmd FROM install_cmds where os_name=\'' + os_name + '\' and app_name=\'' + app + '\'')
		d.add_run_command(c.fetchone()[0])

	return jsonify({'dockerfile' : d.create_dockerfile()})

def post_commands(request):

	d = Dockerfile('', request.json['initial'])

	if request.json['type'] == 'COPY':
		d.add_file(request.json['instruction'])
	elif request.json['type'] == 'RUN':
		d.add_run_command(request.json['instruction'])
	elif request.json['type'] == 'EXPOSE':
		d.add_expose_port(request.json['instruction'])

	return jsonify({'dockerfile' : d.create_dockerfile()})


