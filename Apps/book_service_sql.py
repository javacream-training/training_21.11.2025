import mysql.connector

class Book:
    def __init__(self, book_data: tuple):
        self.isbn: str = book_data[0]
        self.title: str = book_data[1]
        self.price: float = book_data[2]
        self.available: bool = book_data[3]
    
    def __repr__(self):
        # used for default display format when the whole info for the class is to be displayed. 
        # Custom format can anyway be used in the app as needed.
        return f'(isbn={self.isbn}, title={self.title}, price={self.price}, available={self.available})'

class BooksService:

    def __init__(self):
        self.connection = mysql.connector.connect(
            host = 'javacream.eu',
            port = 3406,
            database = 'javacream',
            user = 'user',
            password = 'user'
        )
        self.cursor = self.connection.cursor()
    
    def search_by(self, isbn: str) -> Book: # "-> Book" is a syntax to give typehint for the return value
        sql_statement = f"SELECT * FROM BOOKS WHERE isbn = '{isbn}'"
        self.cursor.execute(sql_statement)
        responce = self.cursor.fetchone()
        check = str(responce)
        if check == 'none' or check == 'None' or check == 'NONE':
            return ' NOT FOUND!! Enter valid ISBN'
        else:
            book = Book(responce)
            return book
        
    def search_all(self) -> list[Book]:
        sql_statement = f"SELECT * FROM BOOKS"
        self.cursor.execute(sql_statement)
        responce = self.cursor.fetchall()
        # books = []
        # for data in responce:
        #     book = Book(data)
        #     books.append(book)   
        # return books
        return [Book(data) for data in responce]



