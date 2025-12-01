import mysql.connector

class Person:
    def __init__(self, person_data: tuple):
        self.id: int = person_data[0]
        self.firstname: str = person_data[1]
        self.lastname: str = person_data[2]
        self.height: float = person_data[3]
        self.weight: float = person_data[4]
        self.gender: float = person_data[5]
    
    def __repr__(self):
        # used for default display format when the whole info for the class is to be displayed. 
        # Custom format can anyway be used in the app as needed.
        return f'(ID = {self.id}, Firstname = {self.firstname}, Lastname = {self.lastname}, Height = {self.height}m, Weight = {self.weight}kg, Gender = {self.gender})'

class PeopleService:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host = 'javacream.eu',
            port = 3406,
            database = 'javacream',
            user = 'user',
            password = 'user'
        )
        self.cursor = self.connection.cursor()
    
    def find_by_id(self, id: int) -> Person:
        sql_statement = f"SELECT * FROM PEOPLE WHERE id = '{id}'"
        self.cursor.execute(sql_statement)
        responce = self.cursor.fetchone()
        check = str(responce)
        if check == 'none' or check == 'None' or check == 'NONE':
            return 'NOT FOUND!! Enter valid ID!'
        else:
            person = Person(responce)
            return person

    def find_by_firstname(self, firstname: str) -> list[Person]:
        sql_statement = f"SELECT * FROM PEOPLE WHERE firstname = '{firstname}'"
        self.cursor.execute(sql_statement)
        responce = self.cursor.fetchall()
        check = str(responce)
        if check == 'none' or check == 'None' or check == 'NONE':
            return 'NOT FOUND!! Enter valid Firstname!'
        else:
            return [Person(data) for data in responce]

    def find_by_lastname(self, lastname: str) -> list[Person]:
        sql_statement = f"SELECT * FROM PEOPLE WHERE lastname = '{lastname}'"
        self.cursor.execute(sql_statement)
        responce = self.cursor.fetchall()
        check = str(responce)
        if check == 'none' or check == 'None' or check == 'NONE':
            return 'NOT FOUND!! Enter valid Lastname!'
        else:
            return [Person(data) for data in responce]

    def find_by_height_range(self, height_min: float, height_max: float) -> list[Person]:
        sql_statement = f"SELECT * FROM PEOPLE WHERE height <= '{height_max}' AND height >= '{height_min}'"
        self.cursor.execute(sql_statement)
        responce = self.cursor.fetchall()
        check = str(responce)
        if check == 'none' or check == 'None' or check == 'NONE':
            return 'NOT FOUND!! Enter valid Height Range!'
        else:
            return [Person(data) for data in responce]
        
    def find_by_weight_range(self, weight_min: float, weight_max: float) -> list[Person]:
        sql_statement = f"SELECT * FROM PEOPLE WHERE weight <= '{weight_max}' AND weight >= '{weight_min}'"
        self.cursor.execute(sql_statement)
        responce = self.cursor.fetchall()
        check = str(responce)
        if check == 'none' or check == 'None' or check == 'NONE':
            return 'NOT FOUND!! Enter valid Weight Range!'
        else:
            return [Person(data) for data in responce]

    def find_by_gender(self, gender: str) -> list[Person]:
        sql_statement = f"SELECT * FROM PEOPLE WHERE GENDER = '{gender}'"
        self.cursor.execute(sql_statement)
        responce = self.cursor.fetchall()
        check = str(responce)
        if check == 'none' or check == 'None' or check == 'NONE':
            return 'NOT FOUND!! Enter valid Gender!'
        else:
            return [Person(data) for data in responce]
        
    def find_all(self) -> list[Person]:
        sql_statement = f"SELECT * FROM PEOPLE"
        self.cursor.execute(sql_statement)
        responce = self.cursor.fetchall()
        # books = []
        # for data in responce:
        #     book = Book(data)
        #     books.append(book)   
        # return books
        return [Person(data) for data in responce]

