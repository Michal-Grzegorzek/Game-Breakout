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
        self.waiting = True
        self.screen.listen()
        self.pen = Scoreboard(0, 0)



    def create_blocks(self):
        for y in self.pos_y:
            for x in self.pos_x:
                self.list_of_blocks.append(Blocks(x, y))

    def welcome_start(self):
        self.waiting = True
        # self.pen.goto(0, 0)
        #
        #
        #
        # while self.waiting:
        #     self.screen.bgcolor('black')
        #     self.pen.write('Breakout Game using Python 3 and Turtle\n\n Press the "space" key to continue',
        #                    align='center', font=('Courier', 24, 'normal'))
        #     self.screen.onkey(self.wait_for_keypress, 'space')



        while True:
            print('dupa')
            self.pen.write(f'\t   Breakout Game  \n\n Press the "SPACE" key for start game',
                              align='center', font=('Courier', 20, 'normal'))
            self.screen.onkey(self.wait_for_keypress, "space")
            # self.screen.onkey(self.start_game, "space")

    def wait_for_keypress(self):
        print('waiting')
        self.waiting = False
        print(self.waiting)
        self.start_game()


    def nothing(self):
        pass

    def start_game(self):
        print('d')
        self.pen.write('',
                       align='center', font=('Courier', 20, 'normal'))
        self.waiting = False
        self.screen.onkey(self.nothing, 'space')
        # self.screen.listen()
        # self.pen.write(f'\t   Breakout Game  \n\n Press the "SPACE" key for start game',
        #           align='center', font=('Courier', 20, 'normal'))
        start = True
        self.create_blocks()
        self.screen.onkeypress(self.paddle.paddle_right, "Right")
        self.screen.onkeypress(self.paddle.paddle_left, "Left")
        # pen.clear()
        while start:
            self.pen.clear()
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
                if (i.ycor() - 20 <= self.ball.ycor() <= i.ycor() + 20) and (i.xcor() - 60 < self.ball.xcor() < i.xcor() + 60):
                    self.score.add_score()
                    self.ball.bounce()
                    i.goto(1000, 1000)

            if self.ball.ycor() < -310:
                # pen = Scoreboard(0, 0)
                # pen.write(f'\t   Breakout Game  \n\n Press the "SPACE" key for start game',
                #           align='center', font=('Courier', 20, 'normal'))
                #
                # screen.onkeypress(start_game, "space")
                self.ball.restart_ball()
                self.score.reset_score()

        self.screen.exitonclick()
