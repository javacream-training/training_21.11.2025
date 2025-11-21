import requests

def buch_suche(isbn):

    url = f'http://javacream.eu:8081/api/books{isbn}'
    data = requests.get(url).json()

    return data


def main():
    
#    data = responce.json()
    
    isbn = input('Do you want the full list of books (ALL) or a specific book ISBN: ')
    if isbn == 'ALL':
        data = buch_suche('')
    else:
        isbn = f'/ISBN{isbn}'
        data = buch_suche(isbn)

    if data["available"] == True:
        print(f'The book you are searching has Title: "{data["title"]}". It costs {data["price"]} and is AVAILABLE')
    else:
        print(f'The book you are searching has Title: {data["title"]}. It costs {data["price"]} and is NOT AVAILABLE!')


main()