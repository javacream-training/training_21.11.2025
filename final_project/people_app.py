from people_service import *
def main():
    service = Person_Service()
    identnr = input('Please enter ID to search for: ')
    search_id = int(identnr)
    person = service.find_by_id(search_id)

    if person:
        print(person)
    else:
        print(f'No person found')
main()