#
# Jocelyn Wilson
# 10/14/24
# File Display Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

def main():
    # Constants
    contents=''

    # Open the file
    inFile=open('numbers.txt' , 'r')

    # Read in the data and store in contents
    contents=inFile.read()

    # Display the contents
    print(contents)
 
# Call the main function
main()