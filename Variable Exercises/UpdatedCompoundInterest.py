principal = float(input("Enter the starting principal: \n"))
interest_rate = float(input("Enter the annual interest rate: \n"))

interest_rate /= 100

times_per_year = int(input("How many times per year is the interest compounded? \n"))
years = int(input("For how many years will the account earn interest? \n"))



balance = principal * (1 + (interest_rate / times_per_year)) ** (times_per_year * years)

balance = "$ {:,.2f}".format(balance)

print('At the end of {} years you will have {}'.format(years, balance))