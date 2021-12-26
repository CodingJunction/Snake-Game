from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.speed("fastest")
        self.goto(random.randint(-240,240),random.randint(-240,240))
        self.pendown()

    def refresh(self):
        self.penup()
        self.goto(random.randint(-240,240),random.randint(-240,240))
        self.pendown()