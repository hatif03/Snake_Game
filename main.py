from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake_Game")
screen.tracer(0)
ssnake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(ssnake.up, "Up")
screen.onkey(ssnake.down, "Down")
screen.onkey(ssnake.right, "Right")
screen.onkey(ssnake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ssnake.move()

    # collision with food
    if ssnake.snake_segment[0].distance(food) <= 15:
        food.refresh()
        ssnake.snake_size()
        score.score += 1
        score.display()

    # collision with walls

    if ssnake.snake_segment[0].xcor() > 280 or ssnake.snake_segment[0].xcor() < -280 or ssnake.snake_segment[
        0].ycor() > 270 or ssnake.snake_segment[0].ycor() < -280:
        score.reset()
        score.display()
        ssnake.reset()


    # collision with tail
    for segment in ssnake.snake_segment[1:]:
        if ssnake.snake_segment[0].distance(segment) < 10:
            score.reset()
            score.display()
            ssnake.reset()

screen.exitonclick()
