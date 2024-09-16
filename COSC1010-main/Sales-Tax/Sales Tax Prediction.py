#Jocelyn Wilson
# 9/5/24
# Sales Tax Programming Project
# COSC 2409 DNT
#

# Variable declarations

# Constants for the state and county tax rates
stateSalesTax=float('0.05')
countySalesTax=float('0.025')
# Get the amount of the purchase.
saleAmount=float(input('Enter original sale amount:'))
# Calculate the state sales tax.
afterStateSalesTax=float(format(saleAmount*stateSalesTax , '.2f'))
# Calculate the county sales tax.
afterCountySalesTax=float(format(saleAmount*countySalesTax , '.2f'))
# Calculate the total tax.
totalSalesTax=float(format(afterStateSalesTax+afterCountySalesTax , '.2f'))
# Calculate the total of the sale.
totalOfSale=totalSalesTax + saleAmount
# Print information about the sale.
print('saleAmount')
print('After state sales tax:', afterStateSalesTax)
print('After county sales tax:', afterCountySalesTax)
print('Total tax:', totalSalesTax )
print('Sale total:', totalOfSale)
