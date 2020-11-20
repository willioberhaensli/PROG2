from flask import Flask
from flask import render_template
from flask import request

from libs import horosdate
from libs import data

app = Flask("Horosdate")


@app.route("/", methods=['GET', 'POST'])

@app.route("/index", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
    	print(request.form)
    	vorname = request.form['vorname']
    	nachname = request.form['nachname']
    	email = request.form['email']
    	telefon = request.form['telefon']
    	tag = request.form['tag']
    	monat = request.form['monat']
    	jahr = request.form['jahr']
    	stadt = request.form['stadt']
    	stunde = request.form['stunde']
    	minute = request.form['minute']
    	returned_data = horosdate.eintrag_speichern(vorname, nachname, email, telefon, tag, monat, jahr, stunde, minute, stadt)

    return render_template("horosdate.html")


@app.route("/search/<name>")

@app.route("/search", methods=['GET', 'POST'])
def search(name=None):
    return "search"


@app.route("/all")
def add():
    testvariable = "test"
    personen_data = data.load_json()
    print(personen_data)
    return render_template("all.html", testvariable=testvariable, data=personen_data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
