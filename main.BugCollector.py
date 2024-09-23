#
# Jocelyn Wilson
# 9/19/2024
# Bug Collector Programming Project
# COSC 2409 DNT
#
# Initialize variables for bugs and total number of bugs collected.
totalBugsCollected=int(0) # The total amount of bugs collected over 5 days
bugsCollected=int(0) # The amount per day the bug collecter collects

# Get number of bugs collected each day using a for loop.
for range in [1, 2, 3, 4, 5]:
   bugsCollected=float(input('How many bugs did you collect? ' ))
   totalBugsCollected=int(bugsCollected+totalBugsCollected)

# Display the total number of bugs collected.
print('The total amount of bugs collected over 5 days is' , totalBugsCollected)


