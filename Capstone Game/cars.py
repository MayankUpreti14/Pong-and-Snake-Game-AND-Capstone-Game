from turtle import Turtle
import random

CAR_DISTANCE = 10
COLORS = ["red", "yellow", "green", "blue", "black", "orange", "purple"]


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.car_speed = CAR_DISTANCE
        self.goto(300, 300)
        self.all_cars = []

    def create(self):
        random_car = random.randint(1, 6)
        if random_car == 1:
            new_car = Turtle("square")
            new_car.hideturtle()
            new_car.penup()
            y_random = random.randint(-240, 270)
            new_car.goto(x=290, y=y_random)
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.showturtle()
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
