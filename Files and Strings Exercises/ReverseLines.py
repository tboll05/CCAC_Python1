readFile = open('input.txt','r')
writeFile = open('output.txt','w')

for line in readFile:
    line = line.rstrip()
    new_str = line[::-1]

    writeFile.write(new_str)

    print("Line:", line, "reversed is:", new_str)

readFile.close()
writeFile.close()