from turtle import Screen
from game import Game
from paddle import Paddle
from ball import Ball
from blocks import Blocks
from scoreboard import Scoreboard
import time
import turtle

screen = Screen()
screen.setup(800, 600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Breakout Game")
ball = Ball()
score = Scoreboard(0, 250)
# ball.speed("slow")

pos_x = [-350, -249, - 148, -47, 46, 145, 244, 343]

list_of_blocks = []
pos_y = [230, 190, 150, 110, 70]
for y in pos_y:
    for x in pos_x:
        list_of_blocks.append(Blocks(x, y))

paddle = Paddle(-350, 0)

screen.listen()

screen.onkeypress(paddle.paddle_right, "Right")
screen.onkeypress(paddle.paddle_left, "Left")




start = True





def start_game():
    start = True
    pen.clear()
    while start:
        time.sleep(ball.move_speed)

        screen.update()
        ball.move_ball()

        if ball.ycor() > 280:
            ball.bounce()

        if ball.xcor() < -380 or ball.xcor() > 380:
            ball.bounce1()

        if ball.distance(paddle) < 50 and ball.ycor() < -230:
            ball.bounce()

        for i in list_of_blocks:
            if (i.ycor()-20 <= ball.ycor() <= i.ycor()+20) and (i.xcor()-60 < ball.xcor() < i.xcor()+60):
                score.add_score()
                ball.bounce()
                i.goto(1000, 1000)

        if ball.ycor() < -310:
            # pen = Scoreboard(0, 0)
            # pen.write(f'\t   Breakout Game  \n\n Press the "SPACE" key for start game',
            #           align='center', font=('Courier', 20, 'normal'))
            #
            # screen.onkeypress(start_game, "space")
            ball.restart_ball()
            score.reset_score()


pen = Scoreboard(0, 0)
pen.clear()
pen.write(f'\t   Breakout Game  \n\n Press the "SPACE" key for start game',
                      align='center', font=('Courier', 20, 'normal'))

screen.onkeypress(start_game, "space")
screen.exitonclick()
