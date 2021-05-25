from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.penup()
        self.speed("fastest")
        self.color("purple")
        self.refresh()

    def refresh(self):
        x_position = random.randint(-250, 250)
        y_position = random.randint(-250, 250)
        self.goto(x_position, y_position)
