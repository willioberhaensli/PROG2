import json



def eintrag_speichern(vorname, nachname, email, telefon, tag, monat, jahr, stunde, minute, stadt):
    daterliste = klassenkamaraden_lesen()
    daterliste[name] = {"vorname": vorname, "nachname": nachname, "email": email, "telefon": telefonnummer, "tag": geburtstag, "monat": geburtsmonat, "jahr": geburtsjahr, "stunde": stunde, "minute": minute, "stadt": geburtsort}   
    print(daterliste)
    with open('klassenkamaraden.txt', "w", encoding="utf-8") as open_file:
        json.dump(daterliste, open_file)



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
    telefonnummer = form_request.get('telefon')
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

    

