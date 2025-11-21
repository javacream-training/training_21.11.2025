import csv

class Person_Service:
    def __init__(self):
        self.inpath = 'final_project/people_data.csv'
    
    def get_people_data(self):
        people = []
        with open(self.inpath, encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['id'] = int(row['id'])
                row['height'] = float(row['height'])
                row['weight'] = float(row['weight'])
                people.append(row)
        return people

    def find_all(self):
        person_data = self.get_people_data()
        return [Person(data) for data in person_data]
    
    def find_by_id(self, id):
        all_people = self.find_all()
        for person in all_people:
            if person.id == id:
                return person
        return None


    
class Person:
    def __init__(self, person_data_dict : dict):
        self.id: int = person_data_dict['id']
        self.firstname : str = person_data_dict['firstname']
        self.lastname : str = person_data_dict['lastname']
        self.height : float = person_data_dict['height']
        self.weight : float = person_data_dict['weight']
        self.gender : str = person_data_dict['GENDER']
    def __repr__(self):
        return f'Person(id={self.id}, firstname={self.firstname}, lastname={self.lastname}, height={self.height}, weight={self.weight}, GENDER={self.gender})'





