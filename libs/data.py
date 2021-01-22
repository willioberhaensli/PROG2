import json

# daten aus json laden für all lovers

def load_json():
    json_daten = {}
    
    try:
        #Json-File öffnen/lesen
        with open('data/data.json') as open_file:
            json_daten = json.load(open_file)
    
    #wenn data.json noch leer ist
    except FileNotFoundError:     
        json_daten = {
		  "personen": {
		    "person": {
		    }}}


    return json_daten

# json-daten werden ins json gespeichert

def save_to_json(daten):
    with open('data/data.json', "w", encoding="utf-8") as open_file:
        json.dump(daten, open_file)

# wenn der datensatz gelöscht werden soll (button auf all lovers)

def clear_json():
    empty_json_structure = json_daten = {
          "personen": {
            "person": {
            }}}
            
    with open('data/data.json', "w", encoding="utf-8") as open_file:
        json.dump(empty_json_structure, open_file)