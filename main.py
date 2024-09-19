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

# Create the snake
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

# Main loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.13)
    # Move the snake forward
    snake.move()

    #Detect Collison with food
    if snake.head.distance(food)<17:
        food.refresh()
        snake.extend()
        scoreboard.increase()

    #Detect Collison with wall
    x_cor = snake.head.xcor()
    y_cor = snake.head.ycor()
    if x_cor<-290 or x_cor>290 or y_cor<-290 or y_cor>290:

        scoreboard.reset()
        snake.reset()

    #Detect Collison with snake
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
