A tetris remake with pygame.

Project Goals

Build a fully functional Tetris remake in Python to practice loops, functions, conditionals, collision detection, and game logic.

Use Pygame to learn the fundamentals of rendering, timing, and interactive input.

Add a user system, where players choose or type their username before the game starts.

Save the top 3 high scores for each user, stored locally (JSON file or text file).

Create clean, readable, modular code using functions and well-organized files.

Learn to use Git and GitHub properly with commit messages, branching, and version control.

Build a project you can show on GitHub as a beginner Python project.

📝 Feature Checklist
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

🔶 Line & Score System

 Detect full rows.

 Clear one or multiple rows.

 Scoring rules:

 40 pts – 1 line

 100 pts – 2 lines

 300 pts – 3 lines

 1200 pts – 4-line clear (Tetris)

 Increase game speed over time.

👤 User System

 Display a menu before starting the game.

 Ask user to enter a username.

 Create user data file if user doesn’t exist.

 Load existing user data for returning users.

🏆 High Score System

 Store user data in a JSON file like:

{
  "Shad": [3200, 2500, 1800],
  "Alex": [4200, 4000, 2000]
}


 After each game:

 Insert the new score.

 Sort scores descending.

 Keep only top three for that user.

 Display player’s top 3 scores on the main menu.

🎨 Graphics & UI

 Draw grid and pieces.

 Color each tetromino.

 Draw hold/next piece box (optional).

 Display current score on screen.

🎮 Controls

 Arrow keys → move left/right/down.

 Up arrow → rotate.

 Escape → return to menu / quit.

 Spacebar → instant drop (optional).

📦 Optional Enhancements

 Add sound effects (rotate, clear line, drop).

 Add a ghost piece (shows where the piece will land).

 Add a hold piece.

 Replace squares with images.

 Difficulty selection.
