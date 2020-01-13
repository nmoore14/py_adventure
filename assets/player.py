class Player:

    # Attributes for the player
    # Name: The players name
    # Age: The players in game age (starting age)
    # Inventory: The items that the player gathers during their quest


    # Create the class
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.inventory = []

    # Add item to inventory method
    def addInventory(self, item):
        self.inventory.append(item)
        # print(self.inventory)

    # Create the player save string
    def savePlayer(self):
        saveString = self.name + "|" + self.age + "|"
        inventoryString = ','.join(self.inventory)
        playerSave = saveString + inventoryString
        return playerSave
