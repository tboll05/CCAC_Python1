#Timothy Bollig
#This program asks the user for the price of a meal and then calculates the 7% tax, 18% tip, and total cost of the meal

foodCost = float(input("Enter the charge for food: "))
tip = foodCost * 0.18
tax = foodCost * 0.07
total = foodCost + tip + tax

print("Tip: ${:,.2f}".format(tip))
print("Tax: ${:,.2f}".format(tax))
print("Total: ${:,.2f}".format(total))