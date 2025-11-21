from book_service import BookService # "import *" importiert alles im Block aus dem Modul from ...
def main():
    book_service = BookService() #BookService muss einem Objekt zugeordnet werden, ansonsten funktioniert es nicht.
    isbn = input('Please enter ISBN you search for or a for all books: ')
    if isbn == "a":
        print(book_service.find_all())
    else:
        print(book_service.search_by(isbn))
main()