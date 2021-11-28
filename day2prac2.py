# Day2 Practical 2
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
print('Average:',average)


if average >= 75:
    if mathGrade < 75:
        if scienceGrade < 75:
            print('You passed the semester, but you need to retake Math and Science subject.')
        elif englishGrade < 75:
            print('You passed the semester, but you need to retake Math and English subject.')
        else:
            print('You passed the semester, but you need to retake Math subject.')
    elif scienceGrade < 75:
        if mathGrade < 75:
            print('You passed the semester, but you need to retake Math and Science subject.')
        elif englishGrade < 75:
            print('You passed the semester, but you need to retake Science and English subject.')
        else:
            print('You passed the semester, but you need to retake Science subject.')
    elif englishGrade < 75:
        if scienceGrade < 75:
            print('You passed the semester, but you need to retake English and Science subject.')
        elif mathGrade < 75:
            print('You passed the semester, but you need to retake Math and English subject.')
        else:
            print('You passed the semester, but you need to retake English subject.')
    else:
        print('Congratulations! You passed the semester.')
else:
    print('Sorry, you failed the semester.')
