from people_service import PeopleService, write_people

def main():
    people_service = PeopleService()
    print(people_service.find_all())
    print(people_service.find_by_id(8))
    print(people_service.find_by_lastname('My'))
    write_people(people_service.find_all())
main()