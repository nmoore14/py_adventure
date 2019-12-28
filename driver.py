# System and OS imports
import sys
import os
import platform

sys.path.append('assets/')
from player import Player

# Global variables
interfacePath = ""

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

def loadGame():
    # Load an existing game

def viewEditGames():
    # View all of the players games that they have saved.

def hack():
    # Load text files for the user to "hack" their current game
    # Figure out how I want to implement this£™£

def exitGame():


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




# The below lines are for testing creating the player object.
name = raw_input("What is your name: ")
new_player = Player(name)

for i in range(0,5):
    new_player.addInventory(str(i))

print(new_player.savePlayer())
