from flask import Flask
import sqlite3
app = Flask(__name__)

@app.route("/")
def hello():
	conn = sqlite3.connect('db.db')
	return "executed"

if __name__ == "__main__":
    app.run()