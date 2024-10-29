#
# Jocelyn Wilson
# 10/22/24
# Exception Handling Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

def main():
    # Declare variables
    total=0.0
    number=0.0
    counter=0

    # Open file numbers.txt to read
    try :
        infile=open('numbers.txt' , 'r')
    except :
        print('A IOError has occured trying to read the file')

    try :
        for line in infile:
            counter=counter+1
            number=float(line)
            print(number)
            total+=number
    except :
        print('A ValueError has occured trying to convert file contents to float numbers')
    
    # Close the file
    infile.close()

    # Calculate the average
    average=total/counter

    # Display the average of the numbers in the file
    print('The average is: ' , average)

# Call main()
main()