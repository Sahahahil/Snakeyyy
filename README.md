# Snakeyyy
A classic snake game with different levels for difficulty; speed and walls

This project is a simple implementation of the classic Snake Game using the Turtle graphics library in Python. The game involves controlling a snake that moves around the screen, trying to eat food to grow longer while avoiding collisions with the screen borders, itself, and potentially walls.

Here's a breakdown of the key components and functionality:

1. **Setup:**
   - The Turtle module is imported for graphics.
   - `delay` is set to control the speed of the game.
   - `score` and `high_score` variables are initialized.
   - The screen is set up with specific dimensions, a background image ("background.png"), and borders.

2. **Snake and Food:**
   - A snake head is created and positioned at the center of the screen.
   - Food is represented as a red circle and placed at a random position on the screen.
   - The player can choose a game level (easy, medium, or hard) at the beginning.

3. **Walls:**
   - Walls are introduced as an additional challenge for medium and hard levels.
   - Vertical and horizontal walls are created, and their positions are randomized.

4. **Functions:**
   - `generate_food_position`: Generates a new position for the food, ensuring it doesn't overlap with walls.
   - `create_wall`: Creates walls with specified characteristics and random positions.
   - `reset_game`: Resets the game state after a collision, allowing the player to choose a new level.
   - `update_score`: Updates the displayed score on the screen.
   - `position_overlaps_with_wall`: Checks if a given position overlaps with any wall.

5. **Keyboard Bindings:**
   - Arrow keys are used to control the snake's movement (up, down, left, right).

6. **Main Game Loop:**
   - The main game loop continuously updates the screen.
   - Collision checks are performed for the snake hitting walls, colliding with itself, and eating food.
   - If the snake collides with something, the game is reset, and the player can choose a new level.

7. **Game Mechanics:**
   - The snake grows longer when it eats food, and the score increases.
   - Speed increases slightly each time the snake eats food.
   - The high score is displayed along with the current score.

8. **Level Selection:**
   - At the start and after each collision, the player is prompted to choose a game level.
   - ![image](https://github.com/Sahahahil/Snakeyyy/assets/152237857/51c4c001-a68f-4d3d-bcc7-72615732554d)
   - The level 1 is as shown as below:
   - ![image](https://github.com/Sahahahil/Snakeyyy/assets/152237857/5b9b10a7-cd2a-4601-8b59-4c2241443fb5)
   - The level 2 is as shown as below:
   - ![image](https://github.com/Sahahahil/Snakeyyy/assets/152237857/f9d080fe-8de8-45d4-b217-de8557526592)
   - The level 3 is as shown as below:
   - ![image](https://github.com/Sahahahil/Snakeyyy/assets/152237857/ba85c999-7f4f-43a4-8435-4b3342795b4b)
  
   - [[Subjected to change later in the future; still in development]]





9. **Graphics:**
   - Turtle graphics are used to draw the snake, food, walls, and borders.
   - The screen is continuously updated to reflect changes in the game state.

10. **Termination:**
    - The game runs indefinitely until manually terminated.

Players can control the snake's movement, collect food, and aim for a high score while facing increased challenges at higher levels.
