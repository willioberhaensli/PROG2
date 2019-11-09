from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for

from libs import horosdate

app = Flask("Horosdate")

@app.route("/")
@app.route("/index", methods=['GET', 'POST'])
def index():
    return render_template("horosdate.html")

@app.route("/search/<name>")
@app.route("/search", methods=['GET', 'POST'])
def search(name=None):
    return "search"

@app.route("/all") 
def add():
    return "all"

if __name__ == "__main__":
    app.run(debug=True, port=5000)