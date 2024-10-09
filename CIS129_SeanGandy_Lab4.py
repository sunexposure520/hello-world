# Module 4 Lab-4
# Sean Gandy
# 10/05/2024
# This application determines the level of employee bonus based on the amount of store earnings

# The main function
def main():
# Declare local variables
    monthlySales = getSales()
    print("monthlySales", monthlySales)
    storeAmount = calcStoreBonus(monthlySales)
    print("storeAmount", storeAmount)
    salesIncrease = getIncrease()
    empAmount = calcEmpBonus(salesIncrease)
    print("salesIncrease", salesIncrease)
    printBonus(storeAmount, empAmount)
    
 # call to getSales (This function gets the monthly sales)
 # call to getIncrease (This function gets the percent of increase in sales
 # call to calcStoreBonus (This function determines the storeAmount bonus)
 # call to printBonus (This function prints the bonus information storeAmount, This function prints the bonus information empAmount)
 # This function gets the monthly sales
def getSales():
    monthlySales = float(input("Please enter sales: "))
    return monthlySales


#This function gets the percent of increase in sales
def getIncrease():    
    salesIncrease = float(input("Enter percent of sales increase using a decimal number: "))
    salesIncrease = salesIncrease / 100
    return salesIncrease



def calcStoreBonus(monthlySales):  
    if monthlySales >= 110000:
        storeAmount = 6000
    elif monthlySales >= 100000:
        storeAmount = 5000
    elif monthlySales >= 90000:
        storeAmount = 4000
    elif monthlySales >= 80000:
        storeAmount = 3000
    else: 
        storeAmount = 0
    return storeAmount



# This function determines the empAmount bonus
def calcEmpBonus(salesIncrease):
    if salesIncrease >= .05:
        empAmount = 75
    elif salesIncrease >= .04:
        empAmount = 50
    elif salesIncrease >= .03:
        empAmount = 40
    else:
        empAmount = 0
    return empAmount

    
# This function prints the bonus information
def printBonus(storeAmount, empAmount):
    print("The store bonus amount is $", storeAmount)
    print("The employee bonus amount is $", empAmount)
    if (storeAmount == 6000) and (empAmount == 75):
        print('Congrats! You have reached the highest bonus amounts possible!')


        
# calls main
main()
        
        
        
...         

