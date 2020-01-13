# Py_Adventure
---
This is my first adventure text based game.

---
### TO-DO:
- [ ] Find an actual name for the game
- [x] Build start screen
- [ ] Build a way to save the game
- [x] Find a way to change the file path based on os
- [ ] Figure out save file method (json?)
- [ ] Figure out how to implement the hack function
- [ ] Update the player class to include the age
---
#### New Game Creation
Info to get from the player
- Name
- Starting age => if the player stays in the game using the same save their age will be increased by a year when needed.
  - This may have an effect on the way the player interacts with the world

#### Save File Example / Description
The save file will be a json file that will have nested objects.
- Player => This will contain the players name and stats
- Inventory => This will contain the players current inventory
- Location => This will store the players location history.
- Save Stats => The date created and the last edited date.

The master file will list the current games as objects.
- Player Name
- Save file name
- Save file location
- Created date
- Last Edited Date
