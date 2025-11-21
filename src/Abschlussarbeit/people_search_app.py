from people import PeopleService

def main():
    people_service = PeopleService()
    user_input = input('Enter an id to select one person, enter "a" for all people, '
                       'enter a lastname to search by lastname, or enter a height range (e.g., "150-180"): ')

    if user_input == 'a':
        people = people_service.find_all()
        print(people)

    elif user_input.isdigit():
        id = int(user_input)
        people = people_service.find_by(id)
        print(people)

    elif '-' in user_input:
        
        try:
            
            min_height_str, max_height_str = user_input.split('-')

            
            if '.' in min_height_str:  
                min_height, max_height = map(float, (min_height_str, max_height_str))
            else:  
                min_height, max_height = map(int, (min_height_str, max_height_str))
                min_height /= 100  
                max_height /= 100  

            people = people_service.find_by_height_range(min_height, max_height)
            if people:
                print(people)
            else:
                print(f"No persons found in the height range {min_height}-{max_height} meters")
        except ValueError:
            print("Invalid height range. Please enter a valid range (e.g., 1.50-1.80 in meters or 150-180 in centimeters).")

    else:
        
        lastname = user_input
        people = people_service.find_by_lastname(lastname)
        print(people)
main()