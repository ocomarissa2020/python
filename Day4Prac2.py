import random

answer = "Y"
while answer.upper() == 'Y':
    print("Welcome to Jack N Poy Game! \n Enter P for Paper \n Enter R for Rock \n Enter S for Scissors.")
    user = str(input("JackNPoy: "))
    computer = ['Rock', 'Paper', 'Scissors']
    for item in range(1):
        r = random.randint(0, 2)
        ci = computer[r]
    if user.upper() == 'P':
        if ci == 'Paper':
            print(f'User: Paper vs Computer: {ci} \n Winner: Tie \n Paper = Paper')
        elif ci == 'Rock':
            print(f'User: Paper vs Computer: {ci} \n Winner: Paper \n Paper covers Rock')
        elif ci == 'Scissors':
            print(f'User: Paper vs Computer: {ci} \n Winner: Scissors \n Scissors cut Paper')
    elif user.upper() == 'R':
        if ci == 'Paper':
            print(f'User: Rock vs Computer: {ci} \n Winner: Paper \n Paper covers Rock')
        elif ci == 'Rock':
            print(f'User: Rock vs Computer: {ci} \n Winner: Tie \n Rock = Rock')
        elif ci == 'Scissors':
            print(f'User: Rock vs Computer: {ci} \n Winner: Rock \n Scissors cannot cut Rock')
    elif user.upper() == 'S':
        if ci == 'Paper':
            print(f'User: Scissors vs Computer: {ci} \n Winner: Scissors \n Scissors cut Paper')
        elif ci == 'Rock':
            print(f'User: Scissors vs Computer: {ci} \n Winner: Rock \n Scissors cannot cut Rock')
        elif ci == 'Scissors':
            print(f'User: Scissors vs Computer: {ci} \n Winner: Tie \n Scissors = Scissors')
    else:
        print("Invalid Bet! Try Again.")
    answer = str(input('Enter Y to try again. Enter any character to exit. '))
