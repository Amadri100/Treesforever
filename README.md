# Tree simulator 🌳
## Summary
1. Tree growing simulation on pygame. Last version as for February 2025.
2. grid based system.
3. Multiple versions...
## General
### run function that runs the code ;p.
- space to pause & play.
- click to appear a 'cell'
- count system to slow down the game
## Versions
### First
First attempt to simulate the grown of a tree.
### extra1
Test without vertical growth
### second
**Now Each cell in either leaves or trunk**
- Added green leaves.
## DOCS
### Variables
**This is a list of most important variables**
- Colors: 
Pygame uses rgb for colors. (red, green, blue)
- Width & Height:
Selects windows size.
- grid width & height:
This variables are used to create the grid and calculate when cells are out of bounds.
- Til_size
The higher this number each tile will be bigger. 
### Classes
**CELLS**
This class has only one argument. Type, type 1 cells are leaves type 0 cells are the trunk.
**ad_grid function**
Adds cells to the grid. 
Using a match statement to know what type the cells is and determine how it will grow.