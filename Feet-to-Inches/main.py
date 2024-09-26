#
# Jocelyn Wilson
# 9/23/2024
# Feet to Inches Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program.

# Constants
conversionRate=12 # The converter between feet and inches

# Variable Declarations
feet=0 # Starting number of feet
inches=0 # Ending number of inches

# Get number of feet to convert
feet=int(input('What is the number of feet that are going to be converted?'))

# Define function feetToInches
def feetToInches():
    inches=feet*conversionRate
    # Display the number of inches
    print('The converted number of inches is' , inches)

# Call function feetToInches to convert the previous number of feet 
feetToInches()

