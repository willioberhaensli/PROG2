from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for

from libs import horosdate, data, destiny

app = Flask("Horosdate")

"""
Startseite, Index-Startseite
Inspriration: https://github.com/aliciafaeh/prog2
"""

@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def index():

        # Wenn Formular ausgefüllt, Daten in JSON, Weiterleitung auf All

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
        
        # Daten in JSON File speichern, Funktion eintrag_speichern in horosdate

        returned_data = horosdate.eintrag_speichern(vorname, nachname, email, telefon, tag, monat, jahr, stunde, minute, stadt)

        # Weiterleitug auf All, primar key mail mitnehmen

        return redirect(url_for('all', email=email))

        # Wenn nicht ausgefüllt, Startseite Laden 

    else:
        return render_template("horosdate.html")


# findlover/destiny page

@app.route("/search", methods=['GET', 'POST'])
@app.route("/search/", methods=['GET', 'POST'])
@app.route("/search/<email>", methods=['GET', 'POST'])
def search(email=None):

    # wenn email ausgefüllt, dann wird auf eigene seite geleitet mit dem eigenen get-parameter
    # if wenn gerade aufgefüllt, in gleicher session

    if request.method == 'POST':
        destiny_email = request.form['destiny_email']
        return redirect(url_for('search', email=destiny_email))

    # versuchen alle daten laden und matching entsprechend der eingegeben mail-adresse (primary-key)
    # verweis destiny.py

    try:
        alle_personen = data.load_json()
        match_daten = destiny.get_matching(email, alle_personen)


    except:
        match_daten = None
        alle_personen = None

    # match_daten = data.load_json()
    # destiny wird geladen aus matchprozess

    return render_template("destiny.html", match_emails=match_daten, daten=alle_personen, person_email=email)


#ALL_ alle eingegeben daten werden angezeigt, falls vorhanden

@app.route("/all")
@app.route("/all/")
@app.route("/all/<email>", methods=['GET', 'POST'])
def all(email=None):
    person_daten = data.load_json()

    #wenn im gleicher session, dann wird begrüssungssatz formuliert: Hallo willi oberhänsli! Hier geht's zu deinen Matches.

    if email:
        try:
            neue_person_daten = person_daten['personen']['person'][email]
        except:
            neue_person_daten = None

    # keine email im zwischenspeicher, dann kein begrüssungssatz

    else:
        neue_person_daten = None

    # ALL aufrufen mit personendaten und NEUER Person

    return render_template("all.html", daten=person_daten, neue_person=neue_person_daten)


# Button Daten löschen

@app.route("/clear_database")
def clear_database():
    data.clear_json()
    person_daten = data.load_json()

    # keine daten gefunden, falls keine vorhanden

    return render_template("all.html", daten=person_daten)

# wenn z.B. xxx.ch/schnapsistgeil dann auf startseite weitergeleitet und kein 404-page-not-found

@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
