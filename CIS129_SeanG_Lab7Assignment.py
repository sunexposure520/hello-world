# Sean G
# CIS129 Module 7 Assignment
# 10/30/2024



import random

def main():
    """
    Define variables
    Determine player input
    Perform dice roll
    Displays results
    
    """
    print()
    
    # initialize variables
    endProgram = 'no'  # control variable for the loop
    playerOne = 'NO NAME'  # default name for player one
    playerTwo = 'NO NAME'  # default name for player two
    
    # call to inputNames function to get player names
    playerOne, playerTwo = inputNames(playerOne, playerTwo)
    
    # loop to run the game until the user decides to end
    while endProgram == 'no':
        # initialize round variable
        # call to rollDice function to get dice rolls and determine winner
        winnerName = rollDice(playerOne, playerTwo)
        
        # call to displayInfo function to show the winner
        displayInfo(winnerName)
        
        # ask the user if they want to end the program
        endProgram = input('Do you want to end program? (yes/no): ')

def inputNames(playerOne, playerTwo):
    """
    Ask for player names
    
    Parameters:
    playerOne: Name of Player One
    playerTwo: Name of Player Two
    
    Returns:
    Names entered by playerOne and playerTwo
    """
    playerOne = input("Enter the name of Player 1: ")
    playerTwo = input("Enter the name of Player 2: ")
    return playerOne, playerTwo

def rollDice(playerOne, playerTwo):
    """
    Roll dice for each player
    Determine winner based on dice roll
    
    Parameters:
    playerOne (str): Name of player one.
    playerTwo (str): Name of player two.
    
    Returns:
    Display winner's name or show when TIE has occurred
    """
    # get random values for each player's dice roll
    p1number = random.randint(1, 6)
    p2number = random.randint(1, 6)
    
    # determine the winner based on dice rolls
    if p1number > p2number:
        winnerName = playerOne
    elif p2number > p1number:
        winnerName = playerTwo
    else:
        winnerName = "TIE"
    
    return winnerName

def displayInfo(winnerName):
    """
    Display winner's name or if TIE has occurred
    
    Parameters:
    winnerName or TIE
    """
    print("The winner is:", winnerName)

main()
