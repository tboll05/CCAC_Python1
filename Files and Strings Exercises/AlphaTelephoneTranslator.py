#Ask the user to input a phone number in the format XXX-XXX-XXXX
phoneNumber = input("Enter the telephone number in the format XXX-XXX-XXXX: \n")

firstPart = phoneNumber[:-8]
secondPart = phoneNumber[-8:]

#Create a new variable called numericPart
numericPart = ''

#Loop through the second part and based on the numbers, concatenate the correct letter to numericPart
for char in secondPart:
    char = char.lower()

    if char == '-':
        numericPart += char
        continue
    elif char == 'a' or char =='b' or char == 'c':
        char = '2'
        numericPart += char
    elif char == 'd' or char =='e' or char == 'f':
        char = '3'
        numericPart += char
    elif char == 'g' or char =='h' or char == 'i':
        char = '4'
        numericPart += char
    elif char == 'j' or char =='k' or char == 'l':
        char = '5'
        numericPart += char
    elif char == 'm' or char =='n' or char == 'o':
        char = '6'
        numericPart += char
    elif char == 'p' or char =='q' or char == 'r' or char == 's':
        char = '7'
        numericPart += char
    elif char == 't' or char =='u' or char == 'v':
        char = '8'
        numericPart += char
    elif char == 'w' or char =='x' or char == 'y' or char == 'z':
        char = '9'
        numericPart += char

#Concatenate or reassign firstPart and alphaPart to phoneNumber or a new variable and display
newNumber = firstPart + numericPart

print('The phone number is', newNumber)