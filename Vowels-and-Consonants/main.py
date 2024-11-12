#
# Jocelyn Wilson
# 11/7/24
# Vowels and Consonants Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

# Define main function
def main():
    mainString='' # String to count
    vowels='aeiouAEIOU' # what vowels are
    consonants='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' # How many consonants there are
    numVowels=0 # How many vowels there are
    numConsonants=0 # How many consonants there are
    
    # Get the string to count from
    mainString=input('What do you want the number of vowels and consonants counted for? ')

    for char in mainString:
        if char in vowels:
            numVowels +=1
    
    for char in mainString:
        if char in consonants:
            numConsonants +=1
    
    # Display the number of vowels and consonants
    print('The number of vowels is' , numVowels , 'and the number of consonants is ', numConsonants )

# Call the main function
main()