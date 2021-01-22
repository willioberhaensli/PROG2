import json
from libs import data

# macht matches anhand der person bzw. primary-key

def get_matching(email, alle_personen):

    # alle daten von zu matchender person abrufen

    zu_matchende_person = alle_personen['personen']['person'][email]

    # sternzeichen person berechnen mit tag/monat

    astro_sign = get_astrological_sign(zu_matchende_person['tag'], zu_matchende_person['monat'])

    # matching schema wird geladen, priorisierung sternzeichen zu sternzeichen

    astro_matching_schema = load_astro_matching_schema_json()

    if astro_matching_schema:

        # verweis funktion sternzeichen berechnen
        
        matches = get_matches_from_astro_sign(astro_sign, alle_personen, astro_matching_schema)
        print(matches)

        # weiterverarbeitung > zurück main
        return matches

    else:
        return None



# Alle matches anhand matching_prio ausrechnen

def get_matches_from_astro_sign(astro_sign, alle_personen, astro_matching_schema):
    matching_prio = astro_matching_schema[astro_sign]['matching_prio']

    # liste für matches
    
    matches = []

    # Sternzeichen anhand matching prio durchgehen

    for single_astro_sign in matching_prio:

        # Alle Personen durchgehen

        for person in alle_personen['personen']['person']:

            #in separate liste matches speichern wenn match
            #liste ist am anfang lehr, nur wenn auftrag dann zwischengespeichert

            if get_astrological_sign(alle_personen['personen']['person'][person]['tag'], alle_personen['personen']['person'][person]['monat']) == single_astro_sign:
                matches.append(person)

        # wenn 3 oder mehr matches dann aus loop gehen >> nur erste Prio berücksichtigen
        # falls weniger als 3, dann auch auf 2 prio
        # wenn nach 1prio mehr als 3, dann wird zweite nicht ausgeführt

        if len(matches) >= 3:
            break

    return matches


# logik sternzeichen berechnen
# Quelle: https://www.w3resource.com/python-exercises/python-conditional-exercise-38.php

def get_astrological_sign(day, month):
    day = int(day)
    if month == '12':
        astro_sign = 'sagittarius' if (day < 22) else 'capricorn'
    elif month == '01':
        astro_sign = 'capricorn' if (day < 20) else 'aquarius'
    elif month == '02':
        astro_sign = 'aquarius' if (day < 19) else 'pisces'
    elif month == '03':
        astro_sign = 'pisces' if (day < 21) else 'aries'
    elif month == '04':
        astro_sign = 'aries' if (day < 20) else 'taurus'
    elif month == '05':
        astro_sign = 'taurus' if (day < 21) else 'gemini'
    elif month == '06':
        astro_sign = 'gemini' if (day < 21) else 'cancer'
    elif month == '07':
        astro_sign = 'cancer' if (day < 23) else 'leo'
    elif month == '08':
        astro_sign = 'leo' if (day < 23) else 'virgo'
    elif month == '09':
        astro_sign = 'virgo' if (day < 23) else 'libra'
    elif month == '10':
        astro_sign = 'libra' if (day < 23) else 'scorpio'
    elif month == '11':
        astro_sign = 'scorpio' if (day < 22) else 'sagittarius'

    return astro_sign



def load_astro_matching_schema_json():
    json_daten = {}
    
    try:
        #Json-File öffnen/lesen
        with open('libs/astro_matching_schema.json') as open_file:
            json_daten = json.load(open_file)
        
    #wenn data.json noch leer ist
    except FileNotFoundError:
        json_daten = None

    return json_daten