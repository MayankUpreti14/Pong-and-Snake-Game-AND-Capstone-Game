from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(380, 0)
l_paddle = Paddle(-380, 0)

ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

i = 0
is_on = True
while is_on:
    time.sleep(0.08 - 0.002*i)
    screen.update()
    ball.move()

    # Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 350) or (ball.distance(l_paddle) < 50 and ball.xcor() < -350):
        i += 1
        ball.bounce_x()

    # Ball misses the r_paddle
    if ball.xcor() > 380:
        ball.restart()
        score.l_point()

    # Ball misses the l_paddle
    if ball.xcor() < -380:
        i = 0
        ball.restart()
        score.r_point()

screen.exitonclick()
