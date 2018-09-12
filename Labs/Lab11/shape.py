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
    def draw(self,turtle):
        if(self.fill):
            turtle.begin_fill()
            turtle.circle(self.rad)
            turtle.end_fill()
        else:
            turtle.circle(self.rad)

class Display(Circle):
    def __init__(self):
        Circle.__init__(self)
        self.elements = ["Red","Orange","Yellow","Green","Blue","Indigo","Violet"]
        self.shapes = []
        self.myt = turtle.Turtle()
        self.setFilled(True)
        self.Screen = self.myt.getscreen()
        self.myt.speed(0)
        self.Screen.delay(0)
        self.myt.hideturtle()

        self.Screen.onclick(self.mouseEvent)
        self.Screen.listen()
    def mouseEvent(self,x,y):
        self.myt.penup()
        self.myt.goto(x,y)
        self.myt.pendown()

        self.rad = random.randint(10,100)
        random.shuffle(self.elements)
        self.color = self.elements[0]
        self.setFillcolor(self.color)
        self.draw(self.myt)

test = Display()
