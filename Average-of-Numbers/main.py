#
# Jocelyn Wilson
# 10/14/24
# Average of Numbers Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

def main():
    # Declare variables
    total=0.0
    number=0.0
    counter=0

    # Open file numbers.txt to read
    infile=open('numbers.txt' , 'r')

    for line in infile:
        counter=counter+1
        number=float(line)
        print(number)
        total+=number
    
    # Close the file
    infile.close()

    # Calculate the average
    average=total/counter

    # Display the average of the numbers in the file
    print('The average is: ' , average)

# Call main()
main()