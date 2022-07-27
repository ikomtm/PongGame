
import time
from turtle import Screen
from paddle import Paddle
from  ball import Ball
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PongGame')
screen.tracer(0)

user_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(user_paddle.move_up, 'Up')
screen.onkey(user_paddle.move_down, 'Down')
screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, 's')
game_is_on = True
x = 1
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move(x)

    if ball.ycor() > 230:
       x = -1

screen.exitonclick()