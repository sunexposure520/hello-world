
# Variables
DOGS = 10  
BUNS = 8   

import math 

# define main
def main():

    total = getTotalHotDogs()
    dogs_left = (DOGS - total % DOGS) % DOGS
    min_dogs = math.ceil(total / DOGS)
    buns_left = (BUNS - total % BUNS) % BUNS
    min_buns = math.ceil(total / BUNS)
    show_results(dogs_left, min_dogs, buns_left, min_buns)
    
# Total Hot Dogs
def getTotalHotDogs():
    people = int(input("Enter the number of people attending the cookout: "))
    hot_dogs = int(input("Enter the number of hot dogs for each person: "))
    total = people * hot_dogs
    return total

# Show Results
def show_results(dogs_left, min_dogs, buns_left, min_buns):
    print("Minimum packages of hot dogs needed: ", min_dogs)
    print("Minimum packages of hot dog buns needed: ", min_buns)
    print("Hot dogs left over: ", dogs_left)
    print("Hot dog buns left over: ", buns_left)


main()
