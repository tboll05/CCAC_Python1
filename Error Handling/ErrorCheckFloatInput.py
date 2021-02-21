value = input("Enter a float: \n")

if value.isdigit():
    value = input("Error int, Enter a float: \n")
try:
    value = float(value)
except ValueError:
    value = input("Error not int, Enter a float: \n")
try:
    value = float(value)
except ValueError:
    value = input("Error not int, Enter a float: \n")

value = float(value)
print("Success:", value)