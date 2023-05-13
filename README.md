# ArteProgra_A2

This Snake game is written in Python and uses the Turtle library to create the game's graphical interface and objects. The objective of the game is to guide a snake to eat food and grow as much as possible without crashing into the screen edges or its own tail.

The code is divided into several functions:

**update_color():** This function changes the color of the snake and the food randomly. It selects a color at random from a predefined list and assigns that color to the global variables snake_color and food_color.

**update_food():** This function updates the position of the food randomly. It generates a random number between 0 and 7, and if that number is 0, it generates another random number to determine whether to change the x coordinate or the y coordinate of the food. If the selected coordinate is changed, it generates another random number to determine whether the coordinate will move up or down, or left or right.

**change(x, y):** This function is called when the user presses one of the arrow keys on the keyboard. It updates the aim vector with the desired direction, which is then used to move the snake in move().

**inside(head):** This function checks whether the snake's head is inside the boundaries of the game area.

**move():** This is the main function that is called repeatedly to move the snake and update the screen. First, it copies the position of the snake's head into a new variable called head. Then, it moves the head in the direction determined by aim. If the head goes outside the screen boundaries or collides with the snake's body, the game ends. If the head encounters food, the snake grows, and a new piece of food is generated at a random location. If no food is found, the snake moves and loses the last segment of its tail. After updating the game objects, the function calls itself after a brief period of time using the ontimer() function, which makes the game continuously update.

**setup():** This Turtle function is used to initialize the game window. The first parameter defines the window's width, the second defines the height, the third parameter defines the horizontal position of the window on the screen, and the fourth parameter defines the vertical position of the window.

**hideturtle():** This function hides the Turtle cursor, which is used to draw the game objects.

**tracer(False):** This function turns off Turtle's animation so that the game objects are drawn instantly, improving the game's performance.

**listen():** This Turtle function allows the game window to listen for user inputs.

**onkey():** This Turtle function defines a function to be called when a key on the keyboard is pressed.

**done():** This Turtle function keeps the game window open until the user closes it.
