from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)  # turn off animations

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")             # IMPORTANT! (onkeypress) No need to click many times to move paddle
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

ball = Ball()
scoreboard = Scoreboard()


is_game_on = True
while is_game_on:
    time.sleep(ball.velocity)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()
    # Detect collision with paddles
    if ball.distance(right_paddle) < 70 and ball.xcor() > 320 or ball.distance(left_paddle) < 70 and ball.xcor() < -320:
        ball.bounce_x()


    # Detect when the right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # Detect when the left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
