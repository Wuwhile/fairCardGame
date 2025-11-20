'''
src/network should contain functions and classes that manage network connections, 
data transmission, and communication protocols for multiplayer functionality.

functions included in the file should be implemented, whether in this file 
or called from other modules.

in src/network, following functions should be implemented:
- establish connection with another local client
- sending game data to another client
- receiving game data from another client (while calling the game functions to update the game state accordingly)
- closing the connection gracefully

a datapack structure should be defined to standardize the data being sent and received, 
  including the following fields:
  - action type (e.g., "play_card", "draw_card", "end_turn")
  - relevant game data (e.g., card details, game state information)
  - timestamp or sequence number to maintain order and consistency
  - any additional metadata required for synchronization and error handling

  
This file should work as a module roadmap for implementing network functionalities in the game,
with most of the actual code being implemented in other files/modules as needed.
'''

