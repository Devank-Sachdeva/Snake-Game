from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.update()

screen.listen()
screen.onkey(fun= snake.up,key="w")
screen.onkey(fun= snake.down,key="s")
screen.onkey(fun= snake.right,key="d")
screen.onkey(fun= snake.left,key="a")


game_bool = True
while game_bool:
    time.sleep(0.1)
    screen.update()
    
    snake.move()
    if snake.head.distance(food) <15:
        food.refresh()
        scoreboard.update()
        snake.grow()
        
    if (snake.head.xcor() > 285 or
        snake.head.xcor() <-285 or
        snake.head.ycor() > 285 or
        snake.head.ycor() <-285 ):
        
        scoreboard.game_over()
        print(snake.head.xcor())
        print(snake.head.ycor())
        game_bool = False
        
    for body in snake.snakeList[1:]:
        if (snake.head.distance(body)< 10):
            print("hit")
            game_bool = False
            scoreboard.game_over()
    
        
screen.exitonclick()