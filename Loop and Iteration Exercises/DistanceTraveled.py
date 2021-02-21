#Ask the user to input the speed of a vehicle in MPH and the number of hours the vehicle has traveled.

#We will use a loop to calculate and display the distance traveled for each hour of the time period.


#Ask user to input speed in MPH
speed = int(input("Enter the speed of the vehicle in mph: \n"))


#Ask user to input number of hours traveled
hours = int(input("Enter the number of hours traveled: \n"))

print("Hour\tDistance Traveled")
print("------------------------")

#Create a for loop that will iterate for each hour.  In the loop, calculate the total distance traveled through the current hour
for i in range(1, hours + 1):
    distance = float(speed * i)
    print(i,'\t',distance)