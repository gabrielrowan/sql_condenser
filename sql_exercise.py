# Program that reads the content of every file in this directory and write it to a separate .txt file 
# Find out how to access all of the files in this directory
# For each file in the directory, read its contents and write it to a separate .txt file
# When there are no more files that are left to be read in this directory, stop (break clause if necessary)

import os 

sql_strings = []

with os.scandir('C:/Users/gabriel/OneDrive/Programming/SQL Exercise') as files:
    for file in files: 
        file_name, file_extension = os.path.splitext(file)
        if file_extension == '.sql':
            with open(file, 'r') as file:
                sql_strings.append(file.read())


with open('C:/Users/gabriel/OneDrive/Programming/SQL Exercise/output.txt', 'w') as new_file:
    for sql_string in sql_strings:
        new_file.write(sql_string + '\n')

print("Output.txt has now been created")