A tetris remake with pygame.

"""Project Goals"""
Build a fully functional Tetris remake in Python to practice loops, functions, conditionals, collision detection, and game logic.

Use Pygame to learn the fundamentals of rendering, timing, and interactive input.

Add a user system, where players choose or type their username before the game starts.

Save the top 3 high scores for each user, stored locally (JSON file or text file).

Create clean, readable, modular code using functions and well-organized files.

Learn to use Git and GitHub properly with commit messages, branching, and version control.

Build a project you can show on GitHub as a beginner Python project.

"""Feature Checklist"""
✅ Core Game Mechanics

 Create a game window using Pygame.

 Create a 10×20 playfield grid.

 Define all 7 Tetris pieces (Tetrominoes).

 Spawn random pieces.

 Piece movement:

 Move left/right.

 Rotate.

 Accelerate down (soft drop).

 Automatic gravity (piece falls every X ms).

 Collision detection with walls, floor, and stacked blocks.

 Lock piece into the grid when it lands.

 Generate next piece after locking the current one.

"""Line & Score System"""

 Detect full rows.

 Clear one or multiple rows.

 Score system:

 40 pts – 1 line

 100 pts – 2 lines

 300 pts – 3 lines

 1200 pts – 4-line clear (Tetris)

 Increase game speed over time.
