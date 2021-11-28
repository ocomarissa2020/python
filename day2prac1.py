# Day2 Practical 1

name = input('Enter Full Name: ')
mathGrade = int(input('Enter Math Grade: '))
scienceGrade = int(input('Enter Science Grade: '))
englishGrade = int(input('Enter English Grade: '))
average = round((mathGrade+scienceGrade+englishGrade)/3,2)

print()
print('Name:',name)
print('Math:',mathGrade)
print('Science:',scienceGrade)
print('English:',englishGrade)
print('Average:', average)


if average >= 75:
    print('Congratulations, you passed the semester.')
else:
    print('Sorry, you failed the semester.')
