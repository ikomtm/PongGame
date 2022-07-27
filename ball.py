from turtle import Turtle

DIRECT = 1


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()

    def move(self, DIRECT):
        new_x = self.xcor() + (10 * DIRECT)
        new_y = self.ycor() + (10 * DIRECT)
        self.goto(new_x, new_y)
