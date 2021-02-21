#This program asks the user for a number and displays what color that number is on a roulette wheel

number = int(input("Enter a pocket number from 0 to 36: \n"))

if number == 0:
    print('Green')
elif number in range(1,11):
    if number % 2 == 0:
        print('Black')
    else:
        print('Red')
elif number in range(11,19):
    if number % 2 == 0:
        print('Red')
    else:
        print('Black')
elif number in range(19,29):
    if number % 2 == 0:
        print('Black')
    else:
        print('Red')
elif number in range(29,37):
    if number % 2 == 0:
        print('Red')
    else:
        print('Black')
else:
    print('Error: Invalid input')