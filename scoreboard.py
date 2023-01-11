from turtle import Turtle

class ScoreBoard (Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=275)
        self.write(arg=f"Score :{self.score}" , align= "center", font= ('calibri',15,'bold'))
        
        
    def update(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score :{self.score}" , align= "center", font= ('calibri',15,'bold'))
    
    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER",align="center",font= ('calibri',20,'bold'))    