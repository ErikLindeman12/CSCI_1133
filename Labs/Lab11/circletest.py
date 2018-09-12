import turtle
import random

class Shape:
    def __init__(self):
         self.myt = turtle.Turtle()
         self.xcor = self.myt.xcor()
         self.ycor = self.myt.ycor()
         self.myt.hideturtle()
         self.fill = False
    def setFillcolor(self,fill=""):
        self.myt.fillcolor(fill)
    def setFilled(self,fillBool=False):
        if(fillBool):
            self.myt.begin_fill()
            self.fill = True
        else:
            self.myt.end_fill()
            self.fill = False
    def isFilled(self):
        return self.fill
    def done(self):
        scr = self.myt.getscreen()
        scr.exitonclick()

class Circle(Shape):
    def __init__(self,x=0,y=0,r=1):
        Shape.__init__(self)
        self.rad = r
        self.myt.penup()
        self.myt.goto(x,y)
        self.myt.pendown()
    def draw(self):
        if(self.fill):
            self.myt.begin_fill()
            self.myt.circle(self.rad)
            self.myt.end_fill()
        else:
            turtle.circle(self.rad)

test = Circle(10,20,100)
test.draw()
test.done()
