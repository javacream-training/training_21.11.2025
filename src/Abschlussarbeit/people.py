import mysql.connector

class Person:
    def __init__(self, person_data: tuple):
        self.id: int = person_data[0]
        self.firstname: str = person_data[1]
        self.lastname: str = person_data[2]
        self.height: float = person_data[3]
        self.weight: int = person_data[4]
        self.gender: str = person_data[5]

    def __repr__(self):
        return f'Person(id={self.id}, firstname={self.firstname}, lastname={self.lastname}, height={self.height}, weight={self.weight}, gender={self.gender})'


class PeopleService:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='javacream.eu', 
            port=3406,
            database='javacream',
            user='user',
            password='user')
        self.cursor = self.connection.cursor()
    
    def find_all(self) -> list[Person]:
        """ Gibt alle Personen zurück """
        sql = "SELECT * FROM PEOPLE"
        self.cursor.execute(sql)
        datas = self.cursor.fetchall()
        return [Person(data) for data in datas]
    
    def find_by(self, id: int) -> Person:
        """ Findet eine Person anhand ihrer ID """
        sql = f"SELECT * FROM PEOPLE WHERE ID = {id}"
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        if data:  # Wenn eine Person mit dieser ID gefunden wird
            return Person(data)
        return None  # Wenn keine Person mit der ID gefunden wird
    
    def find_by_lastname(self, lastname: str) -> list[Person]:
        """ Findet Personen anhand ihres Nachnamens """
        sql = f"SELECT * FROM PEOPLE WHERE LASTNAME = '{lastname}'"
        self.cursor.execute(sql)
        datas = self.cursor.fetchall()
        return [Person(data) for data in datas]  # Mehrere Personen zurückgeben
    
    def find_by_height_range(self, min_height: float, max_height: float) -> list[Person]:
    
        sql = f"SELECT * FROM PEOPLE WHERE HEIGHT BETWEEN {min_height} AND {max_height}"
        self.cursor.execute(sql)
        datas = self.cursor.fetchall()
        return [Person(data) for data in datas]  # Mehrere Personen im Bereich zurückgeben

