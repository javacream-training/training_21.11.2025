#Data constants (Names for constants only in CAPITAL letters according to standard convention)
person_data = [
    ['Andy', 91.4, 1.75],
    ['Pico', 80.7, 1.85],
    ['Lara', 55, 1.61]
    ]

count = 0

for person in person_data:
    name = person[0]
    weight = person[1]
    height = person[2]
    # name, weight, height = person     'list elements can also be asigned like this

    bmi = weight/(height**2)

    person_data[count].append(round(bmi,2))

    print(f'{name} weighing {weight} kg and {height} m tall has a BMI of {bmi:.2f}')
    count += 1
