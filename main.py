from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for

from libs import horosdate, data, destiny

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
        stunde = request.form['stunde']
        minute = request.form['minute']
        stadt = request.form['stadt']
        rückgabe_string = "Hallo " + vorname + " herzlichen Dank fürs teilnehmen. Du wirst über deinen Sternenverwandten informiert, sobald sich alle deine Klassenkameraden eingetragen haben."
        returned_data = horosdate.eintrag_speichern(vorname, nachname, email, telefon, tag, monat, jahr, stunde, minute, stadt)

        return redirect(url_for('all', email=email))
    else:
        return render_template("horosdate.html")


@app.route("/search")
@app.route("/search/")
@app.route("/search/<email>", methods=['GET', 'POST'])
def search(email=None):
    print(email)
    person_daten = data.load_json()
    return render_template("destiny.html", daten=person_daten)


@app.route("/all")
@app.route("/all/")
@app.route("/all/<email>", methods=['GET', 'POST'])
def all(email=None):
    person_daten = data.load_json()
    if email:
        neue_person_daten = person_daten['personen']['person'][email]
        print(neue_person_daten)
    else:
        neue_person_daten = None

    return render_template("all.html", daten=person_daten, neue_person=neue_person_daten)


@app.route("/clear_database")
def clear_database():
    data.clear_json()
    person_daten = data.load_json()
    return render_template("all.html", daten=person_daten)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
