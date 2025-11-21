def calculate_bmi(weight, height):
    UNDERWEIGHT_LIMIT = 18.5
    NORMALWEIGHT_LIMIT = 22
    OVERWEIGHT_LIMIT = 30

    height = height/100
    bmi = round(weight/height**2, 2)
    
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

    bmi_info = [bmi, bmi_category]


    return bmi_info

def main():

    #Data constants (Names for constants only in CAPITAL letters according to standard convention)
    MIN_WEIGHT = 2
    MAX_WEIGHT = 450
    MIN_HEIGHT = 35
    MAX_HEIGHT = 275

    #Data variables (Names for varaibles only in small letters according to standard convention. Variables need not be predefined)
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

        #Data verify
        if (weight_kg < MIN_WEIGHT) or (weight_kg > MAX_WEIGHT):
            print(f'Weight is INVALID! Weight should be between {MIN_WEIGHT} kg and {MAX_WEIGHT} kg')
            validity_flag = False
        if (height_cm < MIN_HEIGHT) or (height_cm > MAX_HEIGHT):
            print(f'Height is INVALID! Height should be between {MIN_HEIGHT} cm and {MAX_HEIGHT} cm')
            validity_flag = False

        if validity_flag == True: #Data validity precheck
            bmi = calculate_bmi(weight_kg, height_cm)

            #Display output
            if bmi[1] != 'INVALID':
                print(f'{person_name} weighing {weight_kg:.2f} kg and {height_cm:.2f} cm tall has a BMI of {bmi[0]:.2f} and is {bmi[1]}')
            else:
                print(f'BMI is {bmi[1]}!. Please check the inputs!')

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


main()