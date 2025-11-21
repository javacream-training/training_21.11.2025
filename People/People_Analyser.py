inpath = 'D:/Schulungen/Data_Analyst/Python_Training/People/People.txt'
with open(inpath, encoding='utf-8') as people_file:
    content = people_file.read()
names = content.split('\n')

upper_names = [f'{name.upper()}\n' for name in names]
upper_names_outpath = 'D:/Schulungen/Data_Analyst/Python_Training/People/People_Upper.txt'
with open(upper_names_outpath, 'wt', encoding='utf-8') as people_file:
    people_file.writelines(upper_names)

unique_names = {f'{name}\n' for name in names}
unique_names_outpath = 'D:/Schulungen/Data_Analyst/Python_Training/People/People_Unique.txt'
with open(unique_names_outpath, 'wt', encoding='utf-8') as people_file:
    people_file.writelines(unique_names)

name_descriptions = [f'{name} has {len(name)} characters\n' for name in names]
name_descriptions_outpath = 'D:/Schulungen/Data_Analyst/Python_Training/People/People_Descriptions.txt'
with open(name_descriptions_outpath, 'wt', encoding='utf-8') as people_file:
    people_file.writelines(name_descriptions)


