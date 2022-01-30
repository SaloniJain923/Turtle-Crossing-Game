from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard
import time

s = Screen()
s.title("Turtle Crossing Game")
s.setup(width=600, height=600)
s.tracer(0)

player = Player()
car = Car()
score = Scoreboard()

s.listen()
s.onkey(key="Up", fun=player.move)

game_on = True
while game_on:
    time.sleep(0.1)
    s.update()

    car.create_car()
    car.move_cars()

    for i in car.cars:
        if i.distance(player) < 20:
            score.game_over()
            game_on = False

    if player.ycor() == 250:
        player.refresh_player()
        score.update_level()
        car.level_up_cars()


s.exitonclick()
