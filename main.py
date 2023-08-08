from turtle import Screen
from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.bgcolor("Black")
screen.tracer(0)

r_paddle = Paddle((350, 0))

l_paddle = Paddle((-350, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_forward, "Up")
screen.onkey(r_paddle.move_backward, "Down")
screen.onkey(l_paddle.move_forward, "w")
screen.onkey(l_paddle.move_backward, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 390:
        ball.miss_paddle()
        scoreboard.l_point()
    if ball.xcor() < -390:
        ball.miss_paddle()
        scoreboard.r_point()

screen.exitonclick()
