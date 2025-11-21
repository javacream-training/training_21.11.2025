path = 'D:\Schulungen\Data Analyst\Python_Training\Liste.txt'
path_out = 'D:\Schulungen\Data Analyst\Python_Training\Liste_Output.txt'

myfile = open(path, encoding='utf-8') # encoding needed to recognise special and/or modern symbols
file_content = myfile.read()
myfile.close() # Opened files always should be closed as otherwise it is locked for other programs

with open(path, encoding='utf-8') as myfile: # File need not be manually closed with the "with" statement
    file_content = myfile.read()

print(file_content)

with open(path_out, 'wt', encoding='utf-8') as myoutputfile: # 'rt': read text(default), 'wt':write text, 'at': append text
    myoutputfile.write(f'{file_content}\nNANU')
