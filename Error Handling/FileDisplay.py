try:
    infile = open('numbers.txt', 'r')

except IOError:
    print("Incorrect file name.")

try:
    for line in infile:
        line = line.rstrip('\n')
        line = int(line)
except ValueError:
    print("Non-numeric data found in the file")