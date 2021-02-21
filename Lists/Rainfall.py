import statistics

#Start with a list of the months and an empty list for rainfall amounts
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
amounts = []

#Loop through the list, asking for input and appending this input to a new list
for i in range(12):
    rainfallAmount = int(input("Enter the rainfall for " + months[i] + ": \n"))
    amounts.append(rainfallAmount)

#Perform Calculations
total = sum(amounts)
total = "{:.2f}".format(total)
average = statistics.mean(amounts)
average = "{:.2f}".format(average)
highestMonth = months[amounts.index(max(amounts))]
lowestMonth = months[amounts.index(min(amounts))]

#Print output
print("Total rainfall:", total)
print("Average rainfall:", average)
print("Highest rainfall:", highestMonth)
print("Lowest rainfall:", lowestMonth)