from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score, NewGameMessage
import time

screen = Screen()
screen.setup(width=800,height=800)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

user1_paddle = Paddle("left")
user2_paddle = Paddle("right")
user1_score = Score("left")
user2_score = Score("right")
message = NewGameMessage()
ball = Ball()
screen.update()

screen.listen()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.001)
    ball.move()
    screen.onkey(fun=user1_paddle.up, key="w")
    screen.onkey(fun=user1_paddle.down, key="s")
    screen.onkey(fun=user2_paddle.up, key="Up")
    screen.onkey(fun=user2_paddle.down, key="Down")

    # Detect collision with wall
    if ((user1_paddle.ycor() - 50 < ball.ycor() < user1_paddle.ycor() + 50) or
        (user2_paddle.ycor() - 50 < ball.ycor() < user2_paddle.ycor() + 50)) and (
            ((ball.xcor() - user1_paddle.xcor()) < 20)
            or ((user2_paddle.xcor() - ball.xcor()) < 20)):
        ball.paddle_bounce()
    if ball.xcor() > 370 or ball.xcor() < -370:
        if ball.xcor() > 0:
            user1_score.add_score()
        else:
            user2_score.add_score()
        screen.update()
        for i in range(3, 0, -1):
            message.message(i)
            screen.update()
            time.sleep(1)
            message.clear()
        # message.clear()
        ball.game_start()
        # game_on = False
    #     ball.left_right_bounce()
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce()


screen.exitonclick()