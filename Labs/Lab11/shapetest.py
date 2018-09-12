import turtle

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

test = Shape()
test.setFillcolor("purple")
test.setFilled(True)
print(test.isFilled())
test.done()
