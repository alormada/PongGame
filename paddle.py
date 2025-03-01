from turtle import Turtle
import time

class Paddle(Turtle):
    def __init__(self, player):
        super().__init__()
        # self.segments = []
        self.player = player
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        if player == "left":
            self.goto(-350, 0)
        else:
            self.goto(350, 0)

    def up(self):
        if self.ycor() + 50 < 390:
            self.sety(self.ycor() + 20)

    def down(self):
        if self.ycor() - 50 > -390:
            self.sety(self.ycor() - 20)

