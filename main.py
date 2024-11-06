from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Initialize the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

# Create the snake, food, and scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Set up control listeners
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# Main loop
game_is_on = True
speed = 0.13  # Initial speed

while game_is_on:
    screen.update()
    time.sleep(speed)

    # Move the snake forward
    snake.move()

    # Detect Collision with food
    if snake.head.distance(food) < 17:
        food.refresh()
        snake.extend()
        scoreboard.increase()
        # Increase speed slightly for each food consumed
        speed = max(0.05, speed - 0.005)

    # Detect Collision with wall
    x_cor = snake.head.xcor()
    y_cor = snake.head.ycor()
    if x_cor < -290 or x_cor > 290 or y_cor < -290 or y_cor > 290:
        scoreboard.show_game_over()
        scoreboard.reset()
        snake.reset()
        speed = 0.13  # Reset speed

    # Detect Collision with snake itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.show_game_over()
            scoreboard.reset()
            snake.reset()
            speed = 0.13  # Reset speed

screen.exitonclick()
