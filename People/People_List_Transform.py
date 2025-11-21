path = 'D:\Schulungen\Data_Analyst\Python_Training\People\People.txt'
path_out = 'D:\Schulungen\Data_Analyst\Python_Training\People\People_Upper.txt'

with open(path, encoding='utf-8') as myfile: # File need not be manually closed with the "with" statement
    file_content = myfile.read()
    file_content = file_content.split('\n')

    
    name_counter = 0
    for names in file_content:
        file_content[name_counter] = names.upper()
        name_counter += 1
    
    print(file_content)

with open(path_out, 'wt', encoding='utf-8') as myoutputfile:
    name_counter = 0
    for names in file_content:
        file_content[name_counter] = names.upper()
        name_counter += 1