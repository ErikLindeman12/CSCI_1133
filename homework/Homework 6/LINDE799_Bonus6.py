#Erik Lindeman (LINDE799)
#CSCI 1133
#Homework 6 Bonus







#This code isn't done so there's no point in testing it.

#I didn't delete it in case I come back to it later with free time/for the fun of it.







































import turtle

class insect:
    def __init__(self,l_color,leg_per_body,body_number,size):
        self.leg_per_body = leg_per_body
        self.size = size
        self.leg_color = l_color
        self.body_number = body_number
        self.insect_turtle = turtle.Turtle()
        self.insect_turtle.speed(0)
        self.catipillar_turtle.hideturtle()

    def draw_legs(self,color,per_body,body_number,size):
        print("yeet")
    def display_insect():
        print("yeet")

class Caterpillar(insect):
    def __init__(self,b_color,l_color,size):
        insect.__init__(self,l_color,1,4,size)
        self.catipillar_turtle = turtle.Turtle()
        self.catipillar_turtle.speed(0)
        self.catipillar_turtle.hideturtle()
        self.body_color = b_color
    def draw_body(self,color,size):
        self.catipillar_turtle.penup()
        self.catipillar_turtle.goto(0,-size*5/2)
        self.catipillar_turtle.color(color,color)
        for x in range(5):
            self.catipillar_turtle.begin_fill()
            self.catipillar_turtle.pendown()
            self.catipillar_turtle.circle(size)
            self.catipillar_turtle.end_fill()
            self.catipillar_turtle.penup()
            self.catipillar_turtle.goto(0,self.catipillar_turtle.ycor()+size)
    def draw_antennae(self,color,size):
        self.catipillar_turtle.color(color,color)
        self.catipillar_turtle.penup()
        self.catipillar_turtle.goto(0,5/2*size)
        self.catipillar_turtle.setheading(125)
        self.catipillar_turtle.forward(size)
        self.catipillar_turtle.pendown()
        self.catipillar_turtle.forward(size)
        self.catipillar_turtle.penup()
        self.catipillar_turtle.goto(0,5/2*size)
        self.catipillar_turtle.setheading(55)
        self.catipillar_turtle.forward(size)
        self.catipillar_turtle.pendown()
        self.catipillar_turtle.forward(size)

    def display_Caterpillar(self):
        self.draw_body(self.body_color,self.size)
        insect.display_insect(self)
        self.draw_antennae(self.leg_color,self.size)
        turtle.done()
class Spider(insect):
    def __init__(self,b_color="green",l_color="purple",size=50,e_color="white"):
        insect.__init__(self,l_color,4,1,size)

    def draw_body():
        print("yeet")
    def draw_Eyes():
        print("yeet")
    def display_Spider():
        print("yeet")
class LadyBug(insect):
    def __init__(self,b_color="green",l_color="purple",size=50,d_color="black"):
        insect.__init__(self,l_color,3,1,size)

    def draw_body():
        print("yeet")
    def draw_Dots():
        print("yeet")
    def display_Ladybug():
        print("yeet")

test = Caterpillar("purple","green",50)
test.display_Caterpillar()
