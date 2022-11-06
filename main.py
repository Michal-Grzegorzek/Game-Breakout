from turtle import Screen
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
ball.speed("slow")

pos_x = [-350, -249, - 148, -47, 46, 145, 244, 343]

list_of_blocks = []
pos_y = [230, 190, 150, 110, 70]
for y in pos_y:
    print(y)
    for x in pos_x:
        print(pos_y)
        list_of_blocks.append(Blocks(x, y))

paddle = Paddle(-350, 0)

screen.listen()

screen.onkeypress(paddle.paddle_right, "Right")
screen.onkeypress(paddle.paddle_left, "Left")


game_is_on = True


while game_is_on:

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
        ball.restart_ball()
        score.reset_score()


screen.exitonclick()
