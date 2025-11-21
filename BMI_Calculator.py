#Data constants (Names for constants only in CAPITAL letters according to standard convention)
UNDERWEIGHT_LIMIT = 18.5
NORMALWEIGHT_LIMIT = 22
OVERWEIGHT_LIMIT = 30
MIN_WEIGHT = 2
MAX_WEIGHT = 450
MIN_HEIGHT = 35
MAX_HEIGHT = 275

#Data variables (Names for varaibles only in small letters according to standard convention. Variables need not be predefined)
# bmi_category = ''
# person_name = ''
# weight_kg = 0.0
# height_cm = 0.0
# height_meter = 0.0
# validity_flag = True
recalculate_flag = 'Y'

# while loop
while recalculate_flag == 'Y':
    
    validity_flag = True #Default value for validity_check

    #Data input
    person_name = input('Enter person Name: ')
    weight_kg = input(f'Enter weight for {person_name} in kg: ')
    height_cm = input(f'Enter height for {person_name} in cm: ')

    #Data conversion
    weight_kg = float(weight_kg)
    height_cm = float(height_cm)
    height_meter = height_cm/100

    #Data verify
    if (weight_kg < MIN_WEIGHT) or (weight_kg > MAX_WEIGHT):
        print(f'Weight is INVALID! Weight should be between {MIN_WEIGHT} kg and {MAX_WEIGHT} kg')
        validity_flag = False
    if (height_cm < MIN_HEIGHT) or (height_cm > MAX_HEIGHT):
        print(f'Height is INVALID! Height should be between {MIN_HEIGHT} cm and {MAX_HEIGHT} cm')
        validity_flag = False

    if validity_flag == True: #Data validity precheck
        #BMI calculation (bmi = Body Mass Index)
        bmi = weight_kg/(height_meter**2)

        #BMI categorisation
        if (bmi < 14) or (bmi > 45): #validity check for BMI
            validity_flag = False
            bmi_category = 'INVALID'
        elif (bmi < UNDERWEIGHT_LIMIT):
            bmi_category = 'underweight'
        elif (bmi <= NORMALWEIGHT_LIMIT):
            bmi_category = 'normal weighted'
        elif (bmi <= OVERWEIGHT_LIMIT):
            bmi_category = 'overweight'
        else:
            bmi_category = 'obese'

        #Display output
        if validity_flag != False:
            print(f'{person_name} weighing {weight_kg:.2f} kg and {height_meter:.2f} m tall has a BMI of {bmi:.2f} and is {bmi_category}')
        else:
            print(f'BMI is {bmi_category}!. Please check the inputs!')

    # # Check for recalculation - Variation 1
    # recalculate_flag = input(f'Enter "Y" to calculate BMI again!: ')
    # if recalculate_flag != 'Y':
    #     break
    # Check for recalculation - Variation 2
    recalculate_flag = input(f'Calculate BMI again?(Y/N): ')
    while True: # Check for valid answer
        if (recalculate_flag == 'Y') or (recalculate_flag == 'N'):
            break
        else:
            recalculate_flag = input(f'Enter valid answer. Calculate BMI again?(Y/N): ')
    if recalculate_flag == 'N':
        break

