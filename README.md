**Semsteraaarbeit PROG2**

**Projektidee:** Erstellen eines Horoskop,- Aszendenz,- Monzeichen-Rechners. Durch  diverse Eingaben der Nutzer, wird im Sinne einer Datingseite der perfekte Partner analysiert. Die Datingfunktion basiert auf Sternzeichenkunde und eigenen festgelegten Kriterien. Am Schluss des Semesters sollen meine Mitstudenten ihren Partner in der Klasse finden können. 

<img src="images/Ablaufdiagram_PROG2.jpg" alt="Ablaufdiagram-PROG2" title="Ablaufdiagram">


## Ausgangslage
Studenten haben meistens und besonderns am Anfang des Studiums Probleme bei der Gruppenfindung für Projekte oder einen Lernpartner zu finden :alien: :purple_heart: :alien:. Dafür braucht es ein System bzw. eine Lustige Anwendung, welche auf Basis von wirklich wichtigen wie verlässlichen Daten :sweat_drops:, eine Zuteilung machen kann. Oder wenigstens Anhaltspunkte dafür.

## Funktion/Projektidee
Die Webapplikation soll dem Anwender ermöglichen, seine Erinnerung in textlicher Form zu erfassen und sie zu terminieren. Diese Erinnerungen / Reminder bestehen aus der Notiz, einem Datum (Fälligkeit) und der dafür verantwortlichen Person. Die Applikation setzt sich aus drei Teilen zusammen. 

 - Notiz erfassen
 - Notiz einsehen
 - Notiz löschen

## Installation / Voraussetzungen

`Python 3.7.3` / `Flask==1.1.1` / `Jinja2==2.10.1` / `gspread==3.1.0` / `oauth2client==4.1.3`
- https://github.com/googleapis/oauth2client
- https://github.com/burnash/gspread

Bitte installiere die beiden Packages wie folgt:
> pip install gspread oauth2client

Damit die Applikation verwendet werden kann, muss im Ordner /static eine Datei - `client_secret.json` - abgelegt werden. Diese Datei muss den Serviceaccount (Private Key, Client-ID etc.) enthalten, welche für den Zugriff auf das spreadsheet berechtigt ist.

Um die Applikation zu starten, führe die Date `main.py` aus.


## Anleitung

 - Die Notizen werden durch die Applikation in ein [Google Spreadsheet](https://docs.google.com/spreadsheets/d/1RpGohe8TQ1XF_vHehBqiY8qHROXgtlVR6ozk9we6Blk/edit#gid=152787366) abgelegt und sind somit von überall zugänglich.
 - Das Spreadsheet ist für alle zugänglich (read-only).
 - Die Notiz kann aus max. 40 Zeichen bestehen.
 - Die maximale Anzahl Notizen beträgt 200.
 - Die maximale Anzahl Notizen kann auf Zeile 33 und 50 in libs/gapi.py `worksheet.update_acell('E1', '=ANZAHL2(A1:A200)')` geändert werden. 
 - Die Applikation funktioniert nur, wenn Google Drive verfügbar ist (Offline, Firewall etc.).
 - Die Applikation bezieht bootstrap über das CDN. Falls das CDN nicht erreichbar ist -> Darstellung mangelhaft.

## Workflow

![Workflow](https://github.com/welschmichel/PROGR2/blob/master/workflow/wf.png)
