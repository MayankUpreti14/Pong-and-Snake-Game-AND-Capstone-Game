from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=280)
        self.level = 1
        self.write(f"LEVEL :{self.level}", align="left", font=("Courier", 14, "normal"))

    def inc_level(self):
        self.level += 1
        self.clear()
        self.goto(x=-280, y=280)
        self.write(f"LEVEL :{self.level}", align="left", font=("Courier", 14, "normal"))

    def over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 20, "normal"))
