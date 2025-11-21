import requests

class Book:
    def __init__(self, book_data_dict: dict):
        self.isbn: str = book_data_dict['isbn']
        self.title: str = book_data_dict['title']
        self.price: float = book_data_dict['price']
        self.available: bool = book_data_dict['available']
    
    def __repr__(self):
        # used for default display format when the whole info for the class is to be displayed. 
        # Custom format can anyway be used in the app as needed.
        return f'(isbn={self.isbn}, title={self.title}, price={self.price}, available={self.available})'

class BooksService:

    def __init__(self):
        self.url = 'http://javacream.eu:8081/api/books'
    
    def search_by(self, isbn: str) -> Book: # "-> Book" is a syntax to give typehint for the return value
        url = f'{self.url}/{isbn}'
        responce = requests.get(url).json()
        check = str(responce)
        if check[2:6:1] == 'isbn':
            book = Book(responce)
            return book
        else:
            return ' NOT FOUND!! Enter valid ISBN'
        
    def search_all(self) -> list[Book]:
        url = self.url
        responce = requests.get(url).json()
        # books = []
        # for data in responce:
        #     book = Book(data)
        #     books.append(book)   
        # return books
        return [Book(data) for data in responce]



