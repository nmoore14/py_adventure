# System and OS imports
import sys
import os
import platform

sys.path.append('assets/')
from player import Player

# Global variables
interfacePath = ""
isPlaying = False
player = None

# Clear the screen so that the content stays at the top of the terminal
def clearScreen(system):
    if system == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def interfacePath(systemName):
    if systemName == "Windows":
        return "assets\\interface\\"
    else:
        return "assets/interface/"

# Menu functions
def createNewGame():
    # Create a new game
    name = raw_input("Please enter your characters name: ")
    age = raw_input("Enter character starging age: ")
    return Player(name, age)

def loadGame():
    # Load an existing game
    print("Load Game")

def viewEditGames():
    # View all of the players games that they have saved.
    print("View / Edit Games")

def hack():
    # Load text files for the user to "hack" their current game
    # Figure out how I want to implement this
    print("Hack your game")

def exitGame():
    print("Exiting the game.")
    exit()


# Set the system so the game knows how to clear the terminal screeni
systemName = platform.system()

clearScreen(systemName)

welcomePath = interfacePath(systemName) + "welcome_menu.txt"
print(welcomePath)

def printWelcome(welcomePath):
    with open(welcomePath, 'r') as f:
        for line in f:
            print(line.rstrip())


printWelcome(welcomePath)

# Building the menu select
menu_choices = ["N", "L", "V", "H", "E"]
menu_selection = raw_input("Menu Choice: ")

if menu_selection.upper() in menu_choices:
    if menu_selection.upper() == "N":
        player = createNewGame()
    elif menu_selection.upper() == "L":
        loadGame()
    elif menu_selection.upper() == "V":
        viewEditGames()
    elif menu_selection.upper() == "H":
        hack()
    elif menu_selection.upper() == "E":
        exitGame()
    else:
        print("Invalid choice")


# The below lines are for testing creating the player object.
if player:
    for i in range(0,5):
        player.addInventory(str(i))

    print(player.savePlayer())
