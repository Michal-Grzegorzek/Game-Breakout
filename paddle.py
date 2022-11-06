from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(1, 5)
        self.color("white")
        self.goto(0, -250)

    def paddle_right(self):
        if self.xcor() <= 350:
            self.goto(self.xcor() + 60, self.ycor())

    def paddle_left(self):
        if self.xcor() >= -350:
            self.goto(self.xcor() - 60, self.ycor())
