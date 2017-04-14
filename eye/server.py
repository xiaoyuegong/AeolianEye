#!/usr/bin/env python

from flask import Flask, send_from_directory,jsonify, render_template, request

app = Flask(__name__, static_url_path="/static")
from contextlib import closing
import requests
import json
import MySQLdb
import sys
import datetime
from sqlalchemy.sql import select
import sqlalchemy
import os

@app.route("/")
def index():
	# print(app.root_path)
	# path = os.path.dirname(os.path.abspath(__file__))
	# img_path = os.path.join(path, "Gastly.png")
	# print(img_path)
	return send_from_directory("templates/", "camerahahaha copy.html")

@app.route("/map")
def send_map():
	# print(app.root_path)
	# path = os.path.dirname(os.path.abspath(__file__))
	# img_path = os.path.join(path, "Gastly.png")
	# print(img_path)
	return send_from_directory("templates/", "camerahahaha.html")

@app.route("/data")
def dictionary_download():	
	db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="aeolian")        # name of the data base
	cur = db.cursor()
	cur.execute("SELECT * FROM AeolianSensorA")

	response = ""
	myresult = []
	column = [t[0] for t in cur.description]
	for row in cur.fetchall():
		myjson = {column[0]: row[0], column[1]: row[1], column[2]: row[2]}
		myresult.append(myjson)

	return jsonify(myresult)

if __name__ == "__main__":
    app.run()

# 	# path = os.path.abspath (app.config['TYPO_DICT_PATH'])
# 	# assert os.path.exists (path)
# 	# return send_from_directory (path, filename, as_attachment=True,
#  #         mimetype='application/octet-stream')
# 	engine = create_engine("mysql://root@localhost/aeolian", echo=True)
# 	conn = engine.connect()
# 	connection = MySQLdb.connect(host = "127.0.0.1", user = "root", passwd = "", db = "aeolian")
# 	print("hahahahaha")
# 	cursor = connection.cursor()
# # execute the SQL query using execute() method.
# 	cursor.execute ("select data, time from AeolianSensorA")
# # fetch all of the rows from the query
# 	data = cursor.fetchall()
# # print the rows
# 	for row in data:
# 		print(row[0], row[1])
# # close the cursor object
# 	cursor.close()
# # close the connection
# 	connection.close()
# # exit the program
# 	sys.exit()






