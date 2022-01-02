from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        file=open("text.txt")
        self.score=0
        self.highscore=int(file.read())
        file.close()        
        
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.pendown()
        self.write(f"Score : {self.score}  High Score : {self.highscore}",align="center",font=("Arial",24,"normal"))
        self.hideturtle()

    def incr(self):
        self.score+=1
        if self.score>self.highscore:
            self.highscore=self.score
            with open("text.txt","w") as w:
                w.write(str(self.highscore))
            
        self.clear()
        self.write(f"Score : {self.score}  High Score : {self.highscore}",align="center",font=("Arial",24,"normal"))
        self.hideturtle()
        

        
    def end(self):
       
        self.penup()
        self.goto(0,0)
        self.pendown()
        self.clear()
        self.write(f"Game Over.",align="center",font=("Arial",24,"normal")) 


    def reset(self):
       
        if self.score>self.highscore:
            self.highscore=self.score
            with open("text.txt","w") as w:
                w.write(str(self.highscore))
 
        self.score=0
        self.clear()
        self.write(f"Score : {self.score}  High Score : {self.highscore}",align="center",font=("Arial",24,"normal"))
        self.hideturtle()
        
