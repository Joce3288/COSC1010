#
# Jocelyn Wilson
# 10/29/24
# Magic 8 Ball Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

# Import random module
import random

#  Define main function
def main():
    question='y' # Is there a question to answer
    answer='' # Answer to the question asked picked at random
    responses=[] # list of all the responses from the file 

    # Open file of responses
    responses=list(open('8_ball_responses.txt' , 'r'))


    # While loop to ask questions until they don't have anymore
    while question=='y':
        
    # Ask them their first question
        input('What is your question? ')

    # Display answer to question
        print(random.choice(responses))
        
    # Ask if they have another question to either restart  or end the loop
        
        question==input('Do you have another question? ')
    
        

# Call the main function
main()