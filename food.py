from turtle import Turtle
from random import randint,choice

colors = ["red","orange","yellow","green","blue","purple","white","pink"]
class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color(choice(colors))
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.refresh()
        
    def refresh(self):
        x = randint(-280,280)
        y = randint(-280,280)
        self.color(choice(colors))
        self.goto(x=x,y=y)
        