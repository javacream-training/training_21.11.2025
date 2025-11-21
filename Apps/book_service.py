import requests
class BookService:   
    def __init__(self):
        self.url = 'http://javacream.eu:8081/api/books'
    def search_by(self, isbn): # "self" is necessary if you create a class
        url = f'{self.url}/{isbn}'
        response = requests.get(url)
        data = response.json()
        book = Book(data)
        return book
        #Row 5 to 7 could also be summarized as : 
        #return requests.get(url).json()
    def find_all(self):
        datas = requests.get(self.url).json() #Url to define is not necessary. Use self.url
        #result = []
        #for data in datas:
        #    book = Book(data)
        #result.append(book)
        #return result
        return [Book(data) for data in datas] #Summarized row 15 to 19
    
class Book:
    def __init__(self, book_data_dict : dict):
        self.ISBN: str = book_data_dict['isbn']
        self.title: str = book_data_dict['title']
        self.price: float = book_data_dict['price']
        self.available: bool = book_data_dict['available']
    def __repr__(self):
        return f'Book(isbn={self.ISBN}, title={self.title}, price={self.price}, available={self.available})'