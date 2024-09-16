#
# Jocelyn Wilson
# 9/3/2024
# Sales Prediction Programming Project
# COSC 2409 DNT
#

# Variables to hold the sales total and the profit
interest = 0.23
# Get the amount of projected sales.
rawSales=float(input('Enter the projected sales: '))
# Calculate the projected profit.
profitFromSales=format(rawSales*interest, '.2f')
# Print the projected profit.
print('Sale Profit:',profitFromSales)
