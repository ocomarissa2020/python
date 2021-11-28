def guide():
    print('Last Name (lastname): ', name["lastname"], '\n')


def updatedRecord():
    print('\n===Record has been Updated===')
    print('Last Name: ', name.get("lastname"), '\n')


name = {
    "lastname": ""
}

print("=====Record Keeping App=====")
option = input('Select Menu\n [A] Add Data\n [B] Delete Data\n [Any Key to Exit]\nSelect: ')

while option.upper() != 'A' or option.upper() != "B":
    if option.upper() == 'A':
        print('\n==========Add Record==========')
        guide()
        key = input('Enter Key: ')
        value = input('Enter Value: ')
        name[key] = value
        updatedRecord()
    elif option.upper() == 'B':
        print('\n==========Delete Record==========')
        guide()
        key = input('Enter Key: ')
        name[key] = ""
        updatedRecord()
    else:
        print('Thank You!')
        break
    option = input('Select Menu\n [A] Add Data\n [B] Delete Data\n [Any Key to Exit]\nSelect: ')
