import mysql.connector
import json
from decimal import Decimal

def main():
    connection = mysql.connector.connect(
        host='javacream.eu', 
        port=3406,
        database='javacream',
        user='user',
        password='user'
    )
    
    sql_statement = f"SELECT * FROM PEOPLE"

    cursor = connection.cursor()
    cursor.execute(sql_statement)
    rows = cursor.fetchall()
    connection.close()
    
    
    people_data = []

    
    for row in rows:
        id, firstname, lastname, height, weight, gender = row
        
        # Umwandlung von Decimal zu float für die Berechnung
        if isinstance(weight, Decimal):
            weight = float(weight)
        if isinstance(height, Decimal):
            height = float(height)
        
        bmi = weight / (height ** 2)  
        
        
        person = {
            "id": id,
            "firstname": firstname,
            "lastname": lastname,
            "height": height,
            "weight": weight,
            "gender": gender,
            "bmi": round(bmi, 2)  
        }
        
        
        people_data.append(person)
    
    
    with open('people_bmi.json', 'w', encoding='utf-8') as json_file:
        json.dump(people_data, json_file, ensure_ascii=False, indent=4)
    
    print("Daten wurden in die Datei 'people_bmi.json' gespeichert.")


main()
