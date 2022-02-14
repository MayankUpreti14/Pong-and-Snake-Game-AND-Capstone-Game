from turtle import Screen
import time
from sfood import Food
from scoreboard import Score
from snake import Snake
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.tracer(0)

score = Score()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        score.update()
        snake.add()

    # To detect collision with the wall
    if snake.head.xcor() >= 290 or snake.head.ycor() >= 270 or snake.head.xcor() <= -290 or snake.head.ycor() <= -290:
        # game_is_on = False
        score.restart()
        snake.new()

    # To detect collision with the body
    for i in range(1, len(snake.segments)):
        if snake.head.distance(snake.segments[i]) < 10:
            # game_is_on = False
            score.restart()
            snake.new()
            # snake = Snake()
            break

screen.exitonclick()