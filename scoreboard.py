from turtle import Turtle

FONT = ("arial", 50, "bold")
Y_POSITION = 300

class Score(Turtle):
    def __init__(self, player):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        if player == "right":
            self.goto(100, Y_POSITION)
        else:
            self.goto(-100, Y_POSITION)
        self.print_score()

    def add_score(self):
        self.clear()
        self.score += 1
        self.print_score()

    def print_score(self):
        self.write(arg=f"{self.score}", move=False, align="center", font=FONT)

class NewGameMessage(Turtle):
    def __init__(self):
        super().__init__()

    def message(self, seconds_left):
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 0)
        self.write(arg=f"New game starts in: {seconds_left}".upper(), move=False, align="center", font=("arial", 15, "normal"))
