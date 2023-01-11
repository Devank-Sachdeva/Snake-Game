from turtle import Turtle
SPACE_LENGTH = 20
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POSITIONS = [(0,0),(0,-20),(0,-40)]

class Snake:
    def __init__(self):
        self.snakeList = []
        self.create_snake()
        self.head = self.snakeList[0]
            
    def create_snake(self):
        for i in range(3):
            self.add_body(position=POSITIONS[i])
            
    def move(self):
        for i in range(len(self.snakeList)-1,0,-1):
            prev = self.snakeList[i-1]
            self.snakeList[i].goto(prev.xcor(),prev.ycor())
        self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def add_body(self,position):
        temp = Turtle(shape="square")
        temp.color("white")
        temp.penup()
        temp.speed('fast')
        temp.goto(position)
        self.snakeList.append(temp)
        
    def grow(self):
        self.add_body(position=self.snakeList[-1].position())