from turtle import Turtle
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.INITIAL_LEN = 3
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in START_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(i)
            self.segments.append(new_segment)

    # To increase the body
    def add(self):
        self.INITIAL_LEN += 1
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        x_ns = self.segments[self.INITIAL_LEN - 2].xcor()
        y_ns = self.segments[self.INITIAL_LEN - 2].ycor()
        if self.segments[2].heading() == 0:
            new_segment.goto(x_ns - 20, y_ns)
            self.segments.append(new_segment)
        elif self.segments[2].heading() == 90:
            new_segment.goto(x_ns, y_ns - 20)
            self.segments.append(new_segment)
        elif self.segments[2].heading() == 180:
            new_segment.goto(x_ns + 20, y_ns)
            self.segments.append(new_segment)
        elif self.segments[2].heading() == 270:
            new_segment.goto(x_ns, y_ns + 20)
            self.segments.append(new_segment)

    def new(self):
        for segs in self.segments:
            segs.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.INITIAL_LEN = 3
        self.head = self.segments[0]

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() == 270:
            return
        else:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90:
            return
        else:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() == 0:
            return
        else:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() == 180:
            return
        else:
            self.head.setheading(0)
