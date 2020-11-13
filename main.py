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
    	rückgabe_string = "Hallo " + vorname + nachname + " Herzlichen Dank fürs teilnehmen, du wirst informiert sobald alle deine Klassenkammeraden sich eingetragen haben."
    	returned_data = horosdate.eintrag_speichern(vorname, nachname, email, telefon, tag, monat, jahr, stunde, minute, stadt)
    	return rückgabe_string

    return render_template("horosdate.html")


@app.route("/search/<name>")
@app.route("/search", methods=['GET', 'POST'])
def search(name=None):
    return "search"


@app.route("/all")
def add():
    return render_template("all.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
