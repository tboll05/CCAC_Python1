#This program define a function to take in time in seconds and calculate how far in meters an object would fall for that amount of time
#It then defines and calls a function to display a running total of distance fallen for a 10 second period

def falling_distance(time):
    return "{:.2f}".format(0.5 * 9.8 * (time**2))

def main():
    result = 0
    
    print("Time\tFalling Distance")
    print("-----------------------------")
    
    for i in range(1,11):
        result = falling_distance(i)
        print(i,"\t", result)

main()