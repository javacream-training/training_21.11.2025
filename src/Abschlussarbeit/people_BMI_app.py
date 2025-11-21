import mysql.connector
import json
from decimal import Decimal

def main():
    # Verbindung zur Datenbank herstellen
    connection = mysql.connector.connect(
        host='javacream.eu', 
        port=3406,
        database='javacream',
        user='user',
        password='user'
    )
    
    # SQL-Statement zum Abrufen aller Personen
    sql_statement = f"SELECT * FROM PEOPLE"

    cursor = connection.cursor()
    cursor.execute(sql_statement)
    rows = cursor.fetchall()
    connection.close()
    
    # Liste zur Speicherung der Ergebnisse
    people_data = []

    # Berechnung und Speicherung des BMI für jede Person
    for row in rows:
        id, firstname, lastname, height, weight, gender = row
        
        # Umwandlung von Decimal zu float für die Berechnung
        if isinstance(weight, Decimal):
            weight = float(weight)
        if isinstance(height, Decimal):
            height = float(height)
        
        bmi = weight / (height ** 2)  # BMI-Formel
        
        # Erstellen eines Dictionaries für die Person
        person = {
            "id": id,
            "firstname": firstname,
            "lastname": lastname,
            "height": height,
            "weight": weight,
            "gender": gender,
            "bmi": round(bmi, 2)  # BMI auf 2 Dezimalstellen gerundet
        }
        
        # Hinzufügen der Person zur Liste
        people_data.append(person)
    
    # Speichern der Daten in einer JSON-Datei
    with open('people_bmi.json', 'w', encoding='utf-8') as json_file:
        json.dump(people_data, json_file, ensure_ascii=False, indent=4)
    
    print("Daten wurden in die Datei 'people_bmi.json' gespeichert.")

# Main-Funktion ausführen
main()
