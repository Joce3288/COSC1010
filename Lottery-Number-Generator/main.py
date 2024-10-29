#
# Jocelyn Wilson
# 10/22/24
# Lottery Number Generator Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

import random 

def main():

    # Make list
    numbers=[0]*7
    
    # Generate seven random numbers assign a random integer
    for index in range(7):
            numbers[index]=random.randint(0, 9)
    
    # Get just the numbers from the list numbers
    print('The lottery number is: ' , numbers[:] )
    
# Call the main() function
main()
