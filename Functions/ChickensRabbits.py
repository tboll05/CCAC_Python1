#This program defines a function that takes in the number of heads and number of legs as arguments and returns the number of chicken and rabbits that this could equate to
#It defines a second function that calls the first function and prints out the desired display.

def solve(heads, legs):
    chickens = heads
    rabbits = 0
    
    #Determine how many legs remain if it is assummed that you only have chickens
    legs = legs - (chickens * 2)
    
    #Loop to adjust count of chickens, rabbits, and remaining legs until there are no more available legs
    while legs != 0:
        chickens -= 1
        rabbits += 1
        legs -= 2

    #Return a tuple with the count of chickens and rabbits
    return (chickens, rabbits)

def main():
    #Unpack the tuple
    chickens, rabbits = solve(70, 188)

    print("Chickens", chickens, "Rabbits", rabbits)

main()