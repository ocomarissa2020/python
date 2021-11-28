# def name():
import random

first_names = ['John', 'Mark', 'Chris', 'James', 'Philip']
middle_names = ['Abad', 'Cruz', 'Domingo', 'Ganados', 'Simon']
last_names = ['Reyes', 'Rizal', 'Bonifacio', 'Mabini', 'Luna']
names = []

print('=====Name Generator=====')
response = str(input('Generate Name: Y if Yes, N if No: '))
while response.upper() == 'Y' or response.upper() == 'N':
    if response.upper() == 'Y':
        for item in range(1):
            r = random.randint(0, 4)
            a = first_names[r]
            b = middle_names[r]
            c = last_names[r]
            full_name = str(a) + " " + str(b) + " " + str(c)
            print('Your new name is: ', full_name)
            names.append(full_name)
    elif response.upper() == 'N':
        print('\nThank You!\n')
        for name in names:
            print(name)
        break
    else:
        print('Invalid Option Selected! Application Terminated.')
        break
    response = str(input('Generate Name: Y if Yes, N if No: '))
