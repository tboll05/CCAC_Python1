import re

#Ask user to input a sentence that is run together but the first character of each word is uppercase
text = input("Enter a string: \n")

#Split the string in to a list where each word is a seperate item
wordList = re.findall(r'[A-Z][\W a-z]*', text)

#Combine the words from the list in to a new string with spaces
results = ' '.join(wordList)

#Display new sentence where only the first word is uppercase
print(results.capitalize())