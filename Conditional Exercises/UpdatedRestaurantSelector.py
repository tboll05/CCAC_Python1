#This program asks if anyone in your party is vegetarian, vegan, or gluten free and then provides a list of restraurants that you can go to

#Create a list of all possible restaurants
restaurants = ["Joe's Gourmet Burgers", "Mama's Fine Italian", "Main Street Pizza", "Corner Cafe", "Chef's Kitchen"]

#Ask if anyone in your party has a diet restriction
vegetarian = input("Is anyone in your party a vegetarian? \n").lower()
vegan = input("Is anyone in your party a vegan? \n").lower()
gluten_free = input("Is anyone in your party gluten free? \n").lower()


#eliminate choices that are not vegetarian friendly
if vegetarian == 'yes' or vegetarian == 'y':
    restaurants.remove("Joe's Gourmet Burgers")


#eliminate choices that are not vegan friendly
if vegan == 'yes' or vegan == 'y':
    try:
        restaurants.remove("Joe's Gourmet Burgers")
    except ValueError:
        pass
    restaurants.remove("Mama's Fine Italian")
    restaurants.remove("Main Street Pizza")


#eliminate choices that are not gluten free friendly
if gluten_free == 'yes' or gluten_free == 'y':
    try:
        restaurants.remove("Joe's Gourmet Burgers")
    except ValueError:
        pass
    try:
        restaurants.remove("Mama's Fine Italian")
    except ValueError:
        pass

#print out remaining choices
print("Here are your restaurant choices:")

for item in restaurants:
    print(item)