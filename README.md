# SQL Condenser

## What does SQL Condenser aim to do? 

SQL Condenser aims to collate the sql contained in multiple `.sql` files and condense these into 1 separate `.sql` file. 

As part of a work deployment process, we currently execute the SQL taken from multiple files. This would be quicker and easier if a program could bring together all the SQL that needs to be executed in 1 place.

## Version 1 

```
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

```

### What does this code do? 

* Creates an empty list called 'sql_strings'
* Scans all the files within a specified file path
* Loops over each file found
* For each file, separate variables are created for the main file name and its file extension
* If the file is a `.sql` file, the content of the file is read and added as one item in the array of `sql_strings`

* The program then loops over every sql string item added to this array
* It writes each string to a new file
* A message is printed that the file has been created

## Positive Points about this code 

1) It gets the job done - separate sql files are successfully condensed into 1 separate file
2) This is my first program in Python!
3) I find this line a very clean and neat way to access a file extension `file_name, file_extension = os.path.splitext(file)`

## Points for improvement 

1) The `with open(file, 'r') as file:` is nested inside with `os.scandir('C:/Users/gabriel/OneDrive/Programming/SQL Exercise') as files:`
   I think two many layers of nesting can be messy - Ideally I would find a way to unnest this logic
2) Hardcode file paths - At the moment, the file paths to read to and write from are hard coded. It would be nice to specify the path to read from in a command line argument
3) There are 2 loops - Looping over the read files and then looping over the array to write to the output file. Is there a way to achieve this same goal with less looping? 
