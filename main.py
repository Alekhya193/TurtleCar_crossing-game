import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(player.move,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    #detecting collision with turle and car
    for i in car_manager.all_cars:
        if i.distance(player)<20:
            game_is_on=False
            scoreboard.game_over()

    #player reched other sides
    if player.is_in_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.level()

screen.exitonclick()