#Type Conversion

birthyear = input('What is your birth year? ')
#Calculating Age, need to convert birthyear value from string to int for operation
#birthyear will be contining a string, as it get's input from the user
#To convert string to integer, int(variable) is used.
age = 2022 - int(birthyear)
#Printing Age
print(age)
