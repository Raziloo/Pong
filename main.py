from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

p1 = Paddle((350, 0))
p2 = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(p1.go_up, "Up")
screen.onkey(p1.go_down, "Down")
screen.onkey(p2.go_up, "w")
screen.onkey(p2.go_down, "s")

game_is_on = True
speed = 0.1
while game_is_on:
    time.sleep(speed)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 380:
        ball.reset_position()
        score.raise_score_p2()
        if score.p2_score == 5:
            score.game_over()
            game_is_on = False

    elif ball.xcor() < -380:
        ball.reset_position()
        score.raise_score_p1()
        if score.p2_score == 5:
            score.game_over()
            game_is_on = False

    if ball.distance(p1) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    elif ball.distance(p2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    ball.move()
    screen.update()
screen.exitonclick()
