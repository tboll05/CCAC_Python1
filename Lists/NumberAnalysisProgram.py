import statistics
myList = []

for i in range(20):
    number = int(input("Enter number " + str((i+1)) + " of 20: \n"))
    myList.append(number)

total = sum(myList)
total = "{:,.2f}".format(total)
average = statistics.mean(myList)
average = "{:.2f}".format(average)

print("Low:", float(min(myList)))
print("High:", float(max(myList)))
print("Total:", total)
print("Average:", average)