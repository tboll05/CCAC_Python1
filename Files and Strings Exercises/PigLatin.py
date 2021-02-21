regSentence = input("Enter a string: \n")

myList = regSentence.split()

pigSentence = ''

for item in myList:
    firstLetter = item[0].upper()
    pigWord = item[1:].upper() + firstLetter + 'AY'
    pigSentence += pigWord + ' '

print(pigSentence)