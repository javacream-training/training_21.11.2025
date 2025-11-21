class Book:
    def __init__(self, isbn, title, price, availability):
        self.isbn = isbn
        self.title = title
        self.price = price
        self.availability = availability

def main():

    book1 = Book('ISBN-1', 'Title-1', 17.45, True)



main()