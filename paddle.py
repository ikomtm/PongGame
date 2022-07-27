from turtle import Turtle
START_POSITION = ()

class Paddle(Turtle):

    def __init__(self, START_POSITION):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(START_POSITION)


    def move_up(self):
        if self.ycor() > 230:
            pass
        else:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() < -220:
            pass
        else:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)


