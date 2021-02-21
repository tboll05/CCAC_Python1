#This program asks the user for a temperature in Celsius and displays that temperature converted in to Fahrenheit

celsius = float(input("Enter a Celsius temperature: \n"))
fahrenheit = ((9.0/5.0) * celsius) + 32.0

print("That is equal to {:.2f} degrees Fahrenheit.".format(fahrenheit))






celsius = float(input("Enter a Celsius temperature: \n"))
fahrenheit = ((9.0/5.0) * celsius) + 32.0

print(f"That is equal to {fahrenheit:.2f} degrees in Fahrenheit.")