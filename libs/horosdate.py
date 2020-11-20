import json
from libs import data



def eintrag_speichern(vorname, nachname, email, telefon, tag, monat, jahr, stunde, minute, stadt):
    json_daten = data.load_json()
    alle_personen = json_daten.get('personen', {})
    person = {"vorname": vorname, "nachname": nachname, "email": email, "telefon": telefon, "tag": tag, "monat": monat, "jahr": jahr, "stunde": stunde, "minute": minute, "stadt": stadt}
    alle_personen['person'][vorname] = person
    json_daten["personen"] = alle_personen

    data.save_to_json(json_daten)
    return json_daten

"""

def eintrag_speichern():
  data = []
  with open('data.json', 'r') as f:
     data = json.load(f)
     f.close()
  print data

    p = {}
  for item in recipes:
     if item['name'] == "pumpkin pie":
       print item
       p = item
       print p

  return render_template('horosdate.html')

"""



def klassenkamaraden_lesen():
    data = {}
    try:
        with open('klassenkamaraden.txt', "r") as open_file:
            data = json.load(open_file)
    except:
        print("Error with file!")
    finally:
        return data

def eintrag_speichern_von_formular(form_request):
    print(form_request)
    vorname = form_request.get('nachname')
    nachname = form_request.get('vorname')
    email = form_request.get('email')
    telefon = form_request.get('telefon')
    geburtstag = form_request.get('tag')
    geburtsmonat = form_request.get('monat')
    geburtsjahr = form_request.get('jahr')
    stunde = form_request.get('stunde')
    minute = form_request.get('minute')
    geburtsort = form_request.get('stadt')
    eintrag_speichern(vorname, nachname, email, telefon, tag, monat, jahr, stunde, minute, stadt)


def person_suchen(form_request):
    daterliste = klassenkamaraden_lesen()
    name = form_request.get('vorname')

    if vorname in daterliste:
        return {vorname: daterliste[name]}

    
