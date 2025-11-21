from people import PeopleService

def main():
    people_service = PeopleService()
    user_input = input('Enter an a for all people: ')
    if user_input == 'a':
        people = people_service.find_all()
        print(people)
    else:
 #       people = user_input
 #       people = people_service.search_by() 
        print('none')

main()