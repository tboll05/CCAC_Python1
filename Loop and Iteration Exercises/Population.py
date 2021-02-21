#Ask for starting number of organisms
population = int(input("Starting number of organisms: \n"))

#Ask for average daily increase percentage
percentage = int(input("Average daily increase: \n"))

#Ask for number of days to multiply
days = int(input("Number of days to multiply: \n"))

print("Day Approximate\t\t","Population")

print("-----------------------------------")

print(1, "\t\t\t", population)

for i in range(2, days + 1):
    population = population + (population * (percentage/100))
    print(i, "\t\t\t", population)