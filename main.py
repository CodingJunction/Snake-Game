from turtle import Turtle,Screen
import random
import time
from snake import Snake
from food import Food
from scoreboard import Score
s=Screen()
s.setup(600,600)
s.title('Snake Game')
s.bgcolor("black")
s.tracer(0)
sn=Snake()
s.listen()
sn.move()
s.onkey(sn.up,"Up")
s.onkey(sn.down,"Down")
s.onkey(sn.left,"Left")
s.onkey(sn.right,"Right")

f=Food()
sc=Score()


k=1
while True:
    sn.move()

    if sn.t[0].distance(f)<20:
        print("NOm Nom Nom")
        f.refresh()
        sc.incr()
        sn.add()

    if sn.t[0].xcor()>290 or sn.t[0].xcor()<-290 or sn.t[0].ycor()>290 or sn.t[0].ycor()<-290 :
        
        sc.end()
        break

    for z in range(len(sn.t)):
        if sn.t[0].distance(sn.t[z])<10 and z!=0:
            sc.end()
            k=0
            break

    if k==0:
        break

s.exitonclick()