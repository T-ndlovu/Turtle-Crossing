import time
import random
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager, STARTING_MOVE_DISTANCE
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

cars = []
level = STARTING_MOVE_DISTANCE
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if random.randint(1, 6) == 1:  # 1 in 5 chance each loop
        new_car = CarManager()
        cars.append(new_car)

    for car in cars:
        car.car_move()
        if player.distance(car) < 20:
            scoreboard.reset()
            game_is_on = False

        if player.ycor() >= FINISH_LINE_Y:
            player.reset()
            scoreboard.increase_score()
            car.speed_increase()

screen.exitonclick()
