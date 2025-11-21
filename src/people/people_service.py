import mysql.connector
import json
class Person:
    def __init__(self, person_data):
        self.id = person_data[0]
        self.firstname = person_data[1]
        self.lastname = person_data[2]
        self.height = person_data[3]
        self.weight = person_data[4]
    def __repr__(self):
        return f'Person(id={self.id}, lastname={self.lastname}, firstname={self.firstname}, height={self.height}, weight={self.weight})'
    def get_bmi(self):
        return self.weight /(self.height ** 2)
class PeopleService:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='javacream.eu', 
            port=3406,
            database = 'javacream', 
            user='user',
            password='user'
        )
        self.cursor = self.connection.cursor()

    def find_all(self):
        sql = "select * from PEOPLE"
        self.cursor.execute(sql)
        datas = self.cursor.fetchall()
        return [Person(data) for data in datas]
    
    def find_by_id(self, id):
        sql = f"select * from PEOPLE where id = {id}"
        self.cursor.execute(sql)
        return Person(self.cursor.fetchone())
    
    def find_by_lastname(self, lastname):
        sql = f"select * from PEOPLE where lastname like '%{lastname}%'"
        self.cursor.execute(sql)
        datas = self.cursor.fetchall()
        return [Person(data) for data in datas]
    
def write_people(people):
    data = [{'name': f'{person.firstname} {person.lastname}', 'bmi': float(person.get_bmi())} for person in people]
    with open('people_bmi.json', 'wt', encoding='utf-8') as file:
        json.dump(data, file)