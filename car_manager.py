from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1,2)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.penup()
        self.car_location()
        self.move_distance = MOVE_INCREMENT


    def car_location(self):
        n = random.randint(-260, 280)
        self.goto(320, n)

    def car_move(self):
        self.forward(MOVE_INCREMENT)

    def speed_increase(self):
        self.move_distance += 3