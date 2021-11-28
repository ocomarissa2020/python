# Day 3 Practical 2

wordBank = []
word = str(input('Enter word: '))
wordBank.append(word)
response = str(input('Do you want to add another word? Y if Yes, N if No: '))

if response == 'Y' or response == 'y':
    while response == 'Y' or response == 'y':
        word = str(input('Enter word: '))
        wordBank.append(word)
        response = str(input('Do you want to add another word? Y if Yes, N if No: '))
        continue
if response == 'N' or response == 'n':
    print('Congratulations! You now have', len(wordBank), 'word/s in your WordBank')
    for words in wordBank:
        print(words)
else:
    print('Invalid Choice. Application Terminated!')