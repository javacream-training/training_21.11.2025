from People import PeopleService 

def main():
    people_service = PeopleService()
    search_criteria = input('Enter searching method (Full_List=*(Default), Firstname=F, Lastname=L, ID=id, Height_Range=HR, Weight_Range=WR, Gender=G): ')
    
    if search_criteria == 'id':
        id = input('Enter the ID: ')
        print(f'PERSON {people_service.find_by_id(id)}')    
    elif search_criteria == 'F':
        firstname = input('Enter the Firstname: ')
        people_list = people_service.find_by_firstname(firstname)
        person_count = 1
        for person in people_list:
            print(f'PERSON-{person_count} {person}')
            person_count += 1
    elif search_criteria == 'L':
        lastname = input('Enter the Lastname: ')
        people_list = people_service.find_by_lastname(lastname)
        person_count = 1
        for person in people_list:
            print(f'PERSON-{person_count} {person}')
            person_count += 1
    elif search_criteria == 'HR':
        height_min = input('Enter minimum height in meters: ')
        height_max = input('Enter maximum height in meters: ')
        people_list = people_service.find_by_height_range(height_min, height_max)
        person_count = 1
        for person in people_list:
            print(f'PERSON-{person_count} {person}')
            person_count += 1
    elif search_criteria == 'WR':
        weight_min = input('Enter minimum weight in kg: ')
        weight_max = input('Enter maximum weight in kg: ')
        people_list = people_service.find_by_weight_range(weight_min, weight_max)
        person_count = 1
        for person in people_list:
            print(f'PERSON-{person_count} {person}')
            person_count += 1
    elif search_criteria == 'G':
        gender = input('Enter the gender: ')
        people_list = people_service.find_by_gender(gender)
        person_count = 1
        for person in people_list:
            print(f'PERSON-{person_count} {person}')
            person_count += 1
    else:
        people_list = people_service.find_all()
        person_count = 1
        for person in people_list:
            print(f'PERSON-{person_count} {person}')
            person_count += 1

main()