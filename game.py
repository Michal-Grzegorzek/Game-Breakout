from turtle import Screen
from turtle import Turtle
from ball import Ball
from scoreboard import Scoreboard
from blocks import Blocks
from paddle import Paddle
import time


class Game(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.screen.setup(800, 600)
        self.screen.tracer(0)
        self.screen.bgcolor("black")
        self.screen.title("Breakout Game")
        self.ball = Ball()
        self.score = Scoreboard(0, 250)
        self.list_of_blocks = []
        self.pos_x = [-350, -249, - 148, -47, 46, 145, 244, 343]
        self.pos_y = [230, 190, 150, 110]
        self.paddle = Paddle(-350, 0)
        self.screen.listen()
        self.pen = Scoreboard(0, -30)

    def create_blocks(self):
        self.list_of_blocks.clear()
        self.screen.update()
        for y in self.pos_y:
            for x in self.pos_x:
                self.list_of_blocks.append(Blocks(x, y))
        self.list_of_blocks.append(Blocks(-148, 70))
        self.list_of_blocks.append(Blocks(-47, 70))
        self.list_of_blocks.append(Blocks(46, 70))
        self.list_of_blocks.append(Blocks(145, 70))
        self.list_of_blocks.append(Blocks(-350, 70))
        self.list_of_blocks.append(Blocks(-350, 70))
        self.list_of_blocks.append(Blocks(-350, 30))
        self.list_of_blocks.append(Blocks(-350, -10))
        self.list_of_blocks.append(Blocks(343, 70))
        self.list_of_blocks.append(Blocks(343, 30))
        self.list_of_blocks.append(Blocks(343, -10))

    def welcome_start(self):
        self.pen.clear()
        self.pen.write(f'\t   Breakout Game  \n\n Press the "SPACE" key for start game',
                       align='center', font=('Courier', 20, 'normal'))

        self.screen.onkey(self.start_game, 'space')
        self.screen.mainloop()

    def start_game(self):
        self.pen.clear()
        self.screen.onkey(None, 'space')
        self.create_blocks()
        self.screen.onkeypress(self.paddle.paddle_right, "Right")
        self.screen.onkeypress(self.paddle.paddle_left, "Left")

        while True:
            time.sleep(self.ball.move_speed)
            self.screen.update()
            self.ball.move_ball()

            if self.ball.ycor() > 280:
                self.ball.bounce()

            if self.ball.xcor() < -380 or self.ball.xcor() > 380:
                self.ball.bounce1()

            if self.ball.distance(self.paddle) < 50 and self.ball.ycor() < -230:
                self.ball.bounce()

            for i in self.list_of_blocks:
                if (i.ycor() - 20 <= self.ball.ycor() <= i.ycor() + 20) and\
                        (i.xcor() - 60 < self.ball.xcor() < i.xcor() + 60):
                    self.score.add_score()
                    self.ball.bounce()
                    i.goto(1000, 1000)

            if self.ball.ycor() < -310:
                self.ball.stop_ball()
                for i in self.list_of_blocks:
                    i.goto(1000, 1000)
                self.pen.write(f'\t      Game Over  \n\n \t    Your score: {self.score.score} \n\n'
                               f' Press the "SPACE" key for restart game',
                          align='center', font=('Courier', 20, 'normal'))
                self.screen.onkey(self.restart_game, "space")

    def restart_game(self):
        self.pen.clear()
        self.score.reset_score()
        self.ball.restart_ball()
        self.start_game()
