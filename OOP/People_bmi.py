class Person:
    def __init__(self, firstname, lastname, weight, height):
        self.firstname = str(firstname)
        self.lastname = str(lastname)
        self.weight = float(weight)
        self.height = float(height/100)

        self.bmi = round((self.weight/(self.height**2)), 2)
    # def get_bmi(self):
    #     self.bmi = self.weight/(self.height**2)


def main():

    Person1 =  Person('John', 'Doe', 78.2, 173.6)
    Person2 =  Person('Jane', 'Dawson', 58, 162)

    Person1.firstname = 'Jerry'

    #Person1.get_bmi()

    print(Person1.bmi)


main()