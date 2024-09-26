#
# Jocelyn Wilson
# 9/23/2024
# Kilometer Converter Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

# Constants
conversionRate=0.6214 # The number that will be multiplied to convert the kilometers to miles

# Variable Declarations
kilometers=0 # The number of kilometers to be converted
miles=0 # The converted into miles amount of kilometers

# Get the amount of kilometers to convert
kilometers=float(input('What is the number of kilometers to be converted?'))

# Convert them to miles
miles=kilometers*conversionRate

# Display final mile count
print('The converted number of miles is' , miles)
