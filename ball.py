from turtle import Turtle
import random
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(0, 0)
        self.setheading(random.randint(0, 359))

    def move(self):
        self.forward(0.3)

    def paddle_bounce(self):
        for angle in range(0, 360, 90):
            n_angle = angle + 90
            print(f"ANGLE: {angle}", self.heading())
            if angle <= self.heading() < n_angle:
                if angle == 0:
                    self.setheading(n_angle + self.heading() % 90)
                    break
                elif angle == 90:
                    self.setheading(angle - self.heading() % 90)
                    break
                elif angle == 180:
                    self.setheading(n_angle + 90 - (self.heading() % 90))
                    break
                else:
                    self.setheading(angle - self.heading() % 90)
                    break
            else:
                print("ERROR WALL")

    def bounce(self):
        print(f"Before bounce: {self.heading()}")
        for angle in range(0, 360, 90):
            print(f"Current angle: {angle}")
            n_angle = angle + 90
            if angle <= self.heading() < n_angle:
                if angle == 0:
                    self.setheading((angle - self.heading()) % 360)
                    break
                elif angle == 90:
                    self.setheading(n_angle + 90 - (self.heading() % 90))
                    break
                elif angle == 180:
                    self.setheading(angle - self.heading() % 90)
                    break
                else:
                    self.setheading((n_angle + 90 - (self.heading() % 90)) % 360)
                    break
            else:
                print("ERROR")

        print(f"After bounce: {self.heading()}")