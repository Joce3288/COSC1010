#
# Jocelyn Wilson
# 10/14/24
# Average of Numbers Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

def main():
    # constants
    infile=''
    
    # Variables
    fileNumbers=float
    totalAmountAdded=float(0.0)
    runningTotal=float(0.0)
    averagedNumbers=float

    # Open the file 
    infile=open('numbers.txt' , 'r')

    # Read its contents
    fileNumbers=infile.read()
    for line in infile:
        number= float(line)
        totalAmountAdded=totalAmountAdded+line
        runningTotal=runningTotal+1
    
    # Divide for the average
    averagedNumbers=totalAmountAdded%runningTotal

    print('The average is: ' , averagedNumbers)
        

main()