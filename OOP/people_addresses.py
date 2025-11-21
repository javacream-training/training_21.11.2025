
class address:
    def __init__(self, city, street, housenumber, pincode):
        self.city = str(city)
        self.street = str(street)
        self.housenumber = str(housenumber)
        self.pincode = str(pincode)
        self.fulladdress = str(f'{self.street} {self.housenumber}, {self.pincode} {self.city}')

class person:
    def __init__(self, firstname, lastname, address, weight, height):
        self.firstname = str(firstname)
        self.lastname = str(lastname)
        self.weight = float(weight)
        self.height = float(height/100)
        self.addresses = {address} # this is a set of sddresses. 1 or many

    def say_hello(self):
        addresscount = 0
        for address in self.addresses:
            if addresscount == 0:
                print(f'My name is {self.firstname} {self.lastname}. I live at {address.fulladdress}.')
                addresscount = 1
            else:
                print(f'My name is {self.firstname} {self.lastname}. My additional address is {address.fulladdress}.')
    def get_bmi(self):
        self.bmi = self.weight/(self.height**2)
        return self.bmi

class student(person):
    def __init__(self, firstname, lastname, address, university, weight, height):
        super().__init__(firstname, lastname, address, weight, height)
        self.university = university
    

def main():

    address1 = address('Amsterdam', 'Bobplatz', '22a', 89458)
    address2 = address('Berlin', 'Ludwigstraße', '7', 76456)
    address3 = address('New York', 'Whitehouse Bwd.', '54', 15487)
    person1 =  person('John', 'Doe', address1, 78.2, 173.6)
    person2 =  person('Jane', 'Dawson', address2, 58, 162)
    student1 = student('Jerry', 'Mustermann', address3, 'NYU', 85.5, 180)
    student1.addresses.add(address2)

    person1.say_hello()
    person2.say_hello()
    student1.say_hello()


main()