#
# Jocelyn Wilson
# 9/17/2024
# Budget Analysis Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

# Named constant for initializing while loop
anotherSubtractedExpense= 'y' # The expense that will be added to the total expenses

# Variable Declarations
initialBudget=0 # The starting budget from the user
totalExpenses=0 # The total expenses from the budget
subtractedExpense=0 # The subtraction of one expnense fromt the budget's total

# Get the user's initial budget for the month
initialBudget=float(input('What is your budget for the month? '))

# Get each expense's amount
while anotherSubtractedExpense=='y':
    subtractedExpense=float(input('What is the total of the expense?'))
    totalExpenses=totalExpenses+subtractedExpense
    anotherSubtractedExpense=input('Do you have another expense?')
# Display the user's total expenses
print('Your total expenses were' , totalExpenses)

# Display if the user was over- or underbudget and by how much
if totalExpenses>=initialBudget:
    print('You were overbudget by' , abs(initialBudget-totalExpenses))
else:
    print('You were in budget by' , abs(initialBudget-totalExpenses))
