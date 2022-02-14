from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, -280)
        self.left(90)
        self.shape("turtle")
        self.showturtle()

    def move(self):
        self.forward(10)

    def again(self):
        self.hideturtle()
        self.goto(0, -280)
        self.showturtle()
