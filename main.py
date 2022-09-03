from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snakes = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snakes.up, "Up")
screen.onkey(snakes.down, "Down")
screen.onkey(snakes.left, "Left")
screen.onkey(snakes.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snakes.move_snake()

    if snakes.head.distance(food) < 15:
        # within 15px of food
        score.clear()
        score.track_score()
        food.refresh()
        snakes.extend()

    if snakes.head.xcor() > 295 or snakes.head.xcor() < -295 or snakes.head.ycor() > 295 or snakes.head.ycor() < -295:
        game_is_on = False
        score.game_over()

    for segments in snakes.segments[1:]:
        if snakes.head.distance(segments) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
