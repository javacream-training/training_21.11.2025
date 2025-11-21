
## typing multiple parameters/methods /classes to import can be seperated by ','. To import all use '*'
## directly using 'import book_service' to import all can be done. However, the various parameters must be the called
## as 'book_service.BooksService()' etc..
#from book_service_url import BooksService
from book_service_sql import BooksService 

def main():
    book_service = BooksService()
    isbn = input('Enter ISBN to search specific book or "*" to search all books: ')
    if isbn == '*':
        # print(book_service.search_all())
        books_list = book_service.search_all()
        book_count = 1
        for book in books_list:
            print(f'BOOK{book_count} {book}')
            book_count += 1
    else:
        print(f'BOOK {book_service.search_by(isbn)}')

main()