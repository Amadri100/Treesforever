# Tree simulator 🌳
## Summary
1. Tree growing simulation on pygama(Last version as for February 2025).
2. grid based system.
3. Multiple versions...
4. Color test file to test colors in screen.
## General ✨✨
### run function that runs the code ;p.
- space to pause & play.
- left click - trunk middle click - seeds right click leaves.
- count system to slow down the game
## Versions 🖳
### First
First attempt to simulate the grown of a tree.
### extra1
Test without vertical growth
### second
**Now Each cell in either leaves or trunk**
- Added green leaves.
## DOCS 📓
### Variables ✖️
**This is a list of most important variables**
- Colors: 
Pygame uses rgb for colors. (red, green, blue)
- Width & Height:
Selects windows size.
- grid width & height:
This variables are used to create the grid and calculate when cells are out of bounds.
- Til_size
The higher this number each tile will be bigger. 
- up_frecuency
Changes how fast the program runs. 
- cells.position 
Each object trunk and leaves, have different positions a position is where the cells are located and is also used on the grid calculations
- screen
The screen in which game objects are drawn.
### Classes
**CELLS** 
This class has only one argument. Type, type 1 cells are leaves type 0 cells are the trunk.
**ad_grid function**
Adds cells to the grid. 
Using a match statement to know what type the cells is and determine how it will grow.
- type 0 vertically
- type 1 diagonally and horizontally
*TYF* is a variable used for randomizing the generation of leaves.
For loop in the end is used to add the new position on the self.position variable.
### Functions

**draw_grid**
takes two positions 
runs first position2 that are the leaves
then the trunk and the grid.
col is width row height

**add_Leaves**🍃
- add leaves at the start of the game on the first trunk added
also freezes the leaves grow so in the first update leaves do not grow *twice*

**not_repeat**
- Avoids trunk positions & and leaves positions to colide
Trunks has priority 

**getpos**
- Gets mouse position.
### Run function
**Main Function**
- This function has the game loop.
if running is false the game stops
if playing is false game pauses
calls two cells objects:
-trunk type0
-leaves type1

**count**
While the game is playing count goes up by 1 when it reaches the update frequency it updates the game.
first checks if add_leaves was used before and then it updates the trunk and leaves.

**Events**
Mouse: 
**NOTE:** If another object is added its position must be set to set() again on the run function to avoid any potential issue.
1. Button 0 is left click
2. then button 2 is right click and 1 the middle click
3. button 0 creates or destroy a trunk 
4. button 2 creates or destroys leaves
Keyboard: 
1. Space to pause.
2. c to clean the grid, pause the game and reset the leavespawn variable.