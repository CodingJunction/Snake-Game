from turtle import Turtle,Screen
import random
import time

class Snake(Turtle):
    

    def __init__(self):
        self.s=Screen()
        self.t=[]
        self.c=20
        self.val=0
        for i in range(3):
            self.add()
            

    def add(self):
        self.s.tracer(0)
        t1=Turtle()
        
        t1.color("white")
        t1.shape("square")
        t1.penup()
        t1.goto(self.val-20,0)
        t1.pendown()
        self.val=self.val-20
        self.t.append(t1)
       # self.s.update()

    def move(self):
        
        time.sleep(0.1)
        for a in range(len(self.t)-1,0,-1):
            x=self.t[a-1].xcor()
            y=self.t[a-1].ycor()
            self.t[a].penup()
            self.t[a].goto(x,y)
            self.t[a].pendown()
        self.t[0].penup()
        self.t[0].forward(20)
        self.t[0].pendown()
        self.s.update()
        # for _ in self.t:
        #     _.forward(20)


        

    def up(self):
        if self.t[0].heading()!=270:
            self.t[0].setheading(90)
        

        pass

    def down(self):
        if self.t[0].heading()!=90:
            self.t[0].setheading(270)
        pass

    def left(self):
        if self.t[0].heading()!=0:
            self.t[0].setheading(180)
        pass

    def right(self):
        if self.t[0].heading()!=180:
            self.t[0].setheading(0)
        pass
      



        