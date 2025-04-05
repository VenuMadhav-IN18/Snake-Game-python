import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):

        super().__init__()

        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)


        self.refresh()
    def refresh(self):
        colors = ["red", "yellow", "white"]
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.color(random.choice(colors))





