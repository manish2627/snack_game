from turtle import Screen, Turtle
import time
from snack import Snack
from food import Food
from scorecard import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

snack = Snack()
food = Food()
scorecard = Score()
screen.listen()
screen.onkey(key="w", fun=snack.up)
screen.onkey(key="s", fun=snack.down)
screen.onkey(key="a", fun=snack.left)
screen.onkey(key="d", fun=snack.right)

is_on = True

while is_on:
    screen.update()
    time.sleep(0.1)
    snack.move()
    if snack.head.distance(food) < 17:
        food.refresh()
        snack.indent_snack()
        scorecard.refresh_score()
    if snack.head.xcor() > 280 or snack.head.xcor() < -280 or snack.head.ycor() > 280 or snack.head.ycor() < -280 :
        print("stop")
        is_on = False
        scorecard.game_over()
    if snack.tail_heat():
        is_on = False
        scorecard.game_over()
screen.exitonclick()
