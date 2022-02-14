from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_user, y_user):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(x=x_user, y=y_user)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(y=new_y, x=self.xcor())

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(y=new_y, x=self.xcor())
