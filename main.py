from flask import Flask
from flask import render_template
from flask import request

from libs import horosdate

app = Flask("Horosdate")


@app.route("/")
@app.route("/index", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        eintrag_speichern_von_formular = request.form['vorname']
        rueckgabe_string = "Hallo " + eintrag_speichern_von_formular + " herzlichen Dank fürs teilnehmen. Du wirst über deinen Sternenverwandten informiert, sobald sich alle deine Klassenkameraden eingetragen haben."
        return rueckgabe_string

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
