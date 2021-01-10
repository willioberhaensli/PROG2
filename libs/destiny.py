import json
from libs import data

def get_matching(email, alle_personen):
    zu_matchende_person = alle_personen['personen']['person'][email]
    astro_sign = get_astrological_sign(zu_matchende_person['tag'], zu_matchende_person['monat'])
    astro_matching_schema = load_astro_matching_schema_json()

    if astro_matching_schema:
        matches = get_matches_from_astro_sign(astro_sign, alle_personen, astro_matching_schema)
        print(matches)

        #weiterverarbeitung wenn mehr als 3 matches?
        return matches

    else:
        return None



def get_matches_from_astro_sign(astro_sign, alle_personen, astro_matching_schema):
    matching_prio = astro_matching_schema[astro_sign]['matching_prio']
    matches = []

    # anhand matching prio durchgehen
    for single_astro_sign in matching_prio:
        # für jede prio alle personen durchgehe
        for person in alle_personen['personen']['person']:
            #in separate liste matches speichern wenn match
            if get_astrological_sign(alle_personen['personen']['person'][person]['tag'], alle_personen['personen']['person'][person]['monat']) == single_astro_sign:
                matches.append(person)

        # wenn 3 oder mehr matches dann aus loop gehen
        if len(matches) >= 3:
            break

    return matches



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