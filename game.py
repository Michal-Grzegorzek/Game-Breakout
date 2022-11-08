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
        self.pos_y = [230, 190, 150, 110, 70]
        self.paddle = Paddle(-350, 0)
        self.screen.listen()
        self.pen = Scoreboard(0, -30)

    def create_blocks(self):
        for y in self.pos_y:
            for x in self.pos_x:
                self.list_of_blocks.append(Blocks(x, y))

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
                # pen = Scoreboard(0, 0)
                self.pen.write(f'\t   Breakout Game  \n\n Press the "SPACE" key for start game',
                          align='center', font=('Courier', 20, 'normal'))
                #
                self.screen.onkeypress(self.restart_game, "space")
                # self.ball.restart_ball()
                # self.score.reset_score()

        self.screen.exitonclick()

    def restart_game(self):
        self.pen.clear()
        self.score.reset_score()
        self.ball.restart_ball()
        self.start_game()

