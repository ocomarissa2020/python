# Day 2, Practical 3

years = int(input('How many years in service? '))
office = input('Enter Office: ')


if years >= 10 and office == 'IT':
    print('Amount Given: ', 10000)
elif years >= 10 and office == 'ACCT':
    print('Amount Given: ', 12000)
elif years >= 10 and office == 'HR':
    print('Amount Given: ', 15000)
elif years < 10 and office == 'IT':
    print('Amount Given: ', 5000)
elif years < 10 and office == 'ACCT':
    print('Amount Given: ', 6000)
elif years < 10 and office == 'HR':
    print('Amount Given: ', 7500)
else:
    print('You are not eligible for a bonus.')