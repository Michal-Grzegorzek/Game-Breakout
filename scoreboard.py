from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.goto(x, y)
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.write(f'Score: {self.score}', False, "center", ("Courier", 30, 'normal'))

    def reset_score(self):
        self.score = 0
        self.clear()
        self.write(f'Score: {self.score}', False, "center", ("Courier", 30, 'normal'))

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', False, "center", ("Courier", 30, 'normal'))


