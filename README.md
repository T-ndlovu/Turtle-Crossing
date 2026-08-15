🎮 Game Concept
You control a turtle (the “player”) that starts at the bottom of the screen.

The goal is to cross the road and reach the finish line at the top.

Cars (rectangles) move horizontally across the screen at random speeds and positions.

If the turtle collides with a car → game over.

Each successful crossing increases the score and makes the cars move faster, raising the difficulty.

🧩 Key Components
Player (Turtle object)

Moves up when you press a key (usually the arrow key or “w”).

Resets to the bottom when reaching the finish line.

Cars (CarManager class)

Spawn randomly on the right side of the screen.

Move left across the screen.

Speed increases as the player levels up.

Scoreboard

Displays the current score.

Updates when the player successfully crosses.

Shows “Game Over” when a collision happens.
