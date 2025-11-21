import csv

def calculate_bmi_infos(weight, height):
    
    height = height/100
    bmi = round(weight/height**2, 2)
    
    return bmi

def categorise_bmi(bmi):
    UNDERWEIGHT_LIMIT = 18.5
    NORMALWEIGHT_LIMIT = 22
    OVERWEIGHT_LIMIT = 30

    if (bmi < 14) or (bmi > 45): #validity check for BMI
        bmi_category = 'INVALID'
    elif (bmi < UNDERWEIGHT_LIMIT):
        bmi_category = 'underweight'
    elif (bmi <= NORMALWEIGHT_LIMIT):
        bmi_category = 'normal weighted'
    elif (bmi <= OVERWEIGHT_LIMIT):
        bmi_category = 'overweight'
    else:
        bmi_category = 'obese'
    
    return bmi_category


def get_data_from_file(path):

    with open(path, mode='r', encoding='utf-8') as people_file:

        people = []
        test = csv.DictReader(people_file)
        # Skip header row if there's one
        #next(people_file)  # Uncomment if there's a header
        for row in test:
            print(row)
            row["height"] = int(row["height"])
            row["weight"] = float(row["weight"])
            people.append(row)

        return people

def get_people_data(people_data):
    

    person = []
    for person_data in people_data:
        name, surname, weight, height = person_data.split(',')
        # person_data_list = person_data.split(',')
        # name = person_data_list[0]
        # surname = person_data_list[1]
        # weight = float(person_data_list[2])
        # height = float(person_data_list[3])
        weight = float(weight)
        height = float(height)
        person.append((name, surname, weight, height))
    
    return person

def get_people_result(data):

    person_descriptions = []
    for person in data:
        name, surname, weight, height = person
        bmi = calculate_bmi_infos(weight, height)
        bmi_category = categorise_bmi(bmi)
        description = f'{surname}, {name} weighing {weight}kg and {height}cm tall has a BMI of {bmi} and is {bmi_category}'
        person_descriptions.append(description)

    return person_descriptions

def display_result(result):

    for sentence in result:
        print(sentence)

def main():

    raw_data = get_data_from_file('D:\Schulungen\Data_Analyst\Python_Training\People_Data\people_data_csv.csv')
    full_data = get_people_data(raw_data)
    result = get_people_result(full_data)
    
    display_result(result)

main ()