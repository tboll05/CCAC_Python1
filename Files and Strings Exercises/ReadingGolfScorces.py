file = open('golf.txt', 'r')

counter = 1

for line in file:
    line = line.rstrip('\n')
    
    if counter % 2 != 0:
        print('Name:', line)
    else:
        if line == '73 ':
            line = line.rstrip()
        elif line == '71 ':
            line = line.rstrip()
        print('Golf Score:', line)

    counter += 1

file.close()