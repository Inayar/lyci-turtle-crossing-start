from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        for new_car in range(1, 1000):
            self.color(random.choice(COLORS))
            self.shape('square')
            self.penup()
            self.shapesize(stretch_wid=1, stretch_len=2)
            self.setheading(180)

    def car_move(self):
        self.goto(320, random.randint(-250, 280))
        self.forward(5)
