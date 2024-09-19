#
import math
# Jocelyn Wilson
# 9/12/24
# Hot Dog Cookout Calculator Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

# Variable Declarations

#Constants 
packOfHotDogs=10
packOfHotDogBuns=8

#Local Variables
amountOfPeople=0 # How many people will be there
amountOfHotDogsNeeded=0 # How many hotdogs there has to be
amountOfHotDogBunsNeeded=0 # How many buns there needs to be
minHotDogs=0 # least amount of hot dog packages needed
minHotDogBuns=0 # least amount of hot dog buns packages needed
remainingHotDogs=0 # Hot dogs that aren't used
remainingBuns=0 # Hot dog buns that aren't used
totalAmountOfHotDogsNeeded=0 # How many put together hot dogs there has to be
import math
# Get amount of people attending and number of hotdogs per person
amountOfPeople=float(input('How many people are going to be going to the cookout?'))
totalAmountOfHotDogsNeeded=amountOfPeople*int(input('How many will each person eat? '))

# Get the total buns and hot dogs
amountOfHotDogsNeeded=totalAmountOfHotDogsNeeded*10
amountOfHotDogBunsNeeded=totalAmountOfHotDogsNeeded*8

# Find how many packs of hot dogs and hot dog buns are needed
minHotDogs=(amountOfHotDogsNeeded/packOfHotDogs)
minHotDogBuns=(amountOfHotDogBunsNeeded/packOfHotDogBuns)
# Find out if the amount of hot dogs needs more than one pack of hot dogs
if minHotDogs>=10:
    remainingHotDogs-amountOfHotDogsNeeded/packOfHotDogs
else:
    print('You need one pack of hot dogs and the leftover is' , packOfHotDogs-minHotDogs)
    # The minimum number of packs of hot dogs
# Find if the amount of hot dog buns needed requires more than one pack
if minHotDogBuns>=8:
    remainingBuns-amountOfHotDogBunsNeeded/packOfHotDogBuns
else:
    print('You need one pack of buns and the leftover is' , packOfHotDogBuns-minHotDogBuns)


# Find the number of leftover hot dogs and hot dog buns
remainingHotDogs=packOfHotDogs-minHotDogs
remainingBuns=packOfHotDogBuns-minHotDogBuns

#print(remainingBuns , remainingHotDogs)
# Show the least amount of hot dog packages that can be used
packsOfHotDogsNeeded=totalAmountOfHotDogsNeeded

print('The minimium packs of hot dogs you need is' , round((minHotDogs/10) , 10))

# Show the least amount of hot dog bun packages that be used
print('The minimum packs of buns you need is' , round((minHotDogBuns/8) , 10))
# Show the amount of leftover hot dogs

# Show the amount of leftover hot dog buns