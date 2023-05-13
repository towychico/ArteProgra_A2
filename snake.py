"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *
import random
from freegames import square, vector

COLORS = ["#54457F", "#AC7B84", "#4C243B", "#B84A62", "#F5A6E6"]  # color constants
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
snake_color, food_color = "#54457F", "#F5A6E6"

def update_color():
    """
    The update_color function is used to change the color of the snake and food.
    It does this by randomly choosing a color from a list of colors.

    :return: The colors of the snake and food
    :doc-author: Alvaro
    """

    global snake_color, food_color
    snake_color = random.choice(COLORS)
    food_color = random.choice(COLORS)


def update_food():
    """
    The update_food function is responsible for updating the food's position.
    It does this by randomly generating a number between 0 and 7, and if that number is 0, it will then generate another random
    number between 0 and 1 to determine whether or not to change the x coordinate of the food. If that second random number is
    0, it will then generate a third random number between 0 and 1 to determine whether or not to add 10 pixels (if it's 1) or
    subtract 10 pixels (if it's 2). It does this same process with y coordinates as well.

    :return: None
    :doc-author: Lou
    """

    if random.randint(0, 7) == 0:
        if random.randint(0, 1) == 0:
            if random.randint(0, 1) == 0:
                food.x += 10
            else:
                food.x -= 10
        else:
            if random.randint(0, 1) == 1:
                food.y += 10
            else:
                food.y -= 10


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 10, snake_color)
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 10, snake_color)

    square(food.x, food.y, 10, food_color)
    update()
    update_food()
    update_color()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()