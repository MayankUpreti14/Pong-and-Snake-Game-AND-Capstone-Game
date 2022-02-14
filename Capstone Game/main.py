from turtle import Screen
from player import Player
from cars import Car
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = Car()
score = Score()

screen.listen()
screen.onkey(player.move, "Up")

j = 0
game_is_on = True
while game_is_on:
    car.create()
    time.sleep(0.1)
    screen.update()
    car.move()
    if player.ycor() > 290:
        player.again()
        score.inc_level()
        j += 1
        car.car_speed += 5

    # When turtle hits the car
    for i in car.all_cars:
        if player.distance(i) < 20:
            game_is_on = False
            score.over()

screen.exitonclick()
