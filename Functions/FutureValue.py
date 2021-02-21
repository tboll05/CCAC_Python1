#This program asks the user to input the current value of a savings account, interest rate, and number of months the money will be left to accrue interest
#These values are passed to a function which will return the value in the savings account after the specified time interval

#Define function to calculate future value of account
def calculate_future_value(principal, interest_rate, months):
    interest_rate /= 100
    return principal * ((1 + interest_rate) ** months)

#Ask user for input
principal = float(input("Enter the present value of the account in dollars: \n"))
interest_rate = float(input("Enter the monthly interest rate as a  percentage: \n"))
months = int(input("Enter the number of months: \n"))

#Pass user input to function  100, 5, 12
futureValue = round(calculate_future_value(principal, interest_rate, months), 2)

#Print output
print("The information for your account is:")
print("Present value:", "${:,.2f}".format(principal))
print("Interest Rate: ", "{:.2f}".format(interest_rate), "%")
print("After", months, "months, the value of your account will be", "${:.2f}".format(futureValue))