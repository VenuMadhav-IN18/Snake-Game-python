from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
starting_position=[-20,-40,0]
segments=[]
food=Food()
score=Scoreboard()

snake= Snake()
screen.listen()
screen.onkey(snake.up,key="Up")
screen.onkey(snake.down,key="Down")
screen.onkey(snake.left,key="Left")
screen.onkey(snake.right , key="Right")

is_on=True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food,food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            is_on = False
            score.game_over()
    if snake.head.xcor()>280 or snake.head.ycor()>280 or snake.head.xcor()<-280 or  snake.head.ycor()<-280:
        is_on=False
        score.game_over()
        score.your_score()





screen.exitonclick()