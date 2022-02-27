# 1/ screen
# 2/ paddle (create and move) x 2
# 3/ ball
# 4/ scoreboard
# 5/ bounce when hit side wall
# 6/ point to other opponent when miss
# 7/ detect collision with paddle

from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong II")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()