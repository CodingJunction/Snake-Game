from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.pendown()
        self.write(f"Score : {self.score}",align="center",font=("Arial",24,"normal"))
        self.hideturtle()

    def incr(self):
        self.score+=1
        self.clear()
        self.write(f"Score : {self.score}",align="center",font=("Arial",24,"normal"))
        self.hideturtle()
        
    def end(self):
        #f sn.t[0].xcor()>240 or sn.t[0].xcor()<-240 or sn.t[0].ycor()>240 or sn.t[0].ycor()<-240 :
        self.penup()
        self.goto(0,0)
        self.pendown()
        self.clear()
        self.write(f"Game Over.",align="center",font=("Arial",24,"normal")) 
        
