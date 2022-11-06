from turtle import Turtle
import random


class Blocks(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.colors = ['red', 'lime', 'yellow', 'purple', 'blue', 'pink', 'azure4']
        self.shapesize(1, 4)
        self.color(random.choice(self.colors))
        self.goto(x, y)
