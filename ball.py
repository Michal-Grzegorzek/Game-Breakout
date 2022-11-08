from turtle import Turtle
import time
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.colors = ['red', 'lime', 'yellow', 'purple', 'blue', 'pink', 'azure4']
        self.color(random.choice(self.colors))
        self.penup()
        self.goto(0, -100)
        self.direction = [-4, -3, -2, 2, 3, 4]
        self.x_move, self.y_move = random.choice(self.direction), random.choice([2, 3, 4])
        self.move_speed = 0.01

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
        self.move_speed *= 0.1

    def bounce1(self):
        self.x_move *= -1

    def restart_ball(self):
        self.goto(0, 0)
        self.move_speed = 0.01
        self.x_move *= -1
        self.y_move *= -1

    def stop_ball(self):
        self.goto(1100, 1100)
