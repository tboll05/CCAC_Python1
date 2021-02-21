#Ask user for a non-negative integer
num = int(input("Enter a nonnegative integer: \n"))

#Calculate the factorial of the interger entered
result = 1

for i in range(1, num + 1):
    result *= i

#Display the results
print("The factoral of", num, "is", result)