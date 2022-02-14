from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        # self.high_score = 0
        self.hideturtle()
        self.color("White")
        self.penup()
        self.goto(x=0, y=270)
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 15, "bold"))

    def restart(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.clear()
        self.score = 0
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 15, "bold"))

    def update(self):
        self.clear()
        self.score += 1
        self.goto(x=0, y=270)
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 15, "bold"))