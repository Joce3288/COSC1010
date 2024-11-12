#
# Jocelyn Wilson
# 11/6/24
# Pig Latin Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Define main function
def main():
    sentence='' # Original sentence
    pigLatin=[] # Sentence after being converted
    words='' # Each word in sentence seperated
    newSentence=[] # Each piece of the sentence to put together
    pigLatinSentence=[] # The new sentence in Pig Latin
    # Get user's sentence
    sentence=input('What is your sentence? ')

    # Convert to pig latin
    words=sentence.split()
    for word in words:
        pigLatin=word[1:] + word[0] + 'ay'
        pigLatinSentence.append(pigLatin)
    newSentence=" ".join(pigLatinSentence)
        
    # Display the new sentence
    print('Your new sentence is' , newSentence)

# Call the main function
main()
