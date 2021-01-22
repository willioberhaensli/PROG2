import json
from libs import data

# wir von main ausgerufen, funktion safetojson wird abgespielt
# daten in json format gegliedert

def eintrag_speichern(vorname, nachname, email, telefon, tag, monat, jahr, stunde, minute, stadt):
    json_daten = data.load_json()
    alle_personen = json_daten.get('personen', {})
    person = {"vorname": vorname, "nachname": nachname, "email": email, "telefon": telefon, "tag": tag, "monat": monat, "jahr": jahr, "stunde": stunde, "minute": minute, "stadt": stadt}
    alle_personen['person'][email] = person
    json_daten["personen"] = alle_personen

    data.save_to_json(json_daten)
    return json_daten