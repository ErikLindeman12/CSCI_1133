#Erik Lindeman (LINDE799)
#CSCI 1133
#Homework 6 Problem C

import turtle

class Caterpillar:
    def __init__(self,b_color="green",l_color="purple",size=50):
        #Sets values to the arguments
        self.body_color = b_color
        self.leg_color = l_color
        self.body_size = size
        #Initializes the caterpillar specific turtle
        self.catipillar_turtle = turtle.Turtle()
        self.catipillar_turtle.speed(0)
        self.catipillar_turtle.hideturtle()

    def draw_body(self,size,color):
        #goes to the bottom of the screen and sets the fill color
        self.catipillar_turtle.penup()
        self.catipillar_turtle.goto(0,-size*5/2)
        self.catipillar_turtle.color(color,color)
        for x in range(5):
            #Draws a circle (filled), then moves up once per loop
            self.catipillar_turtle.begin_fill()
            self.catipillar_turtle.pendown()
            self.catipillar_turtle.circle(size)
            self.catipillar_turtle.end_fill()
            self.catipillar_turtle.penup()
            self.catipillar_turtle.goto(0,self.catipillar_turtle.ycor()+size)

    def draw_antennae(self,size,color):
        #Changes color of the fill
        self.catipillar_turtle.color(color,color)
        self.catipillar_turtle.penup()
        #goes to the middle of the head
        self.catipillar_turtle.goto(0,5/2*size)
        #Rotates to the angle, moves to edge of the head, then draws the left antennae
        self.catipillar_turtle.setheading(125)
        self.catipillar_turtle.forward(size)
        self.catipillar_turtle.pendown()
        self.catipillar_turtle.forward(size)
        self.catipillar_turtle.penup()
        #goes to the middle of the head
        self.catipillar_turtle.goto(0,5/2*size)
        #Rotates to the angle, moves to edge of the head, then draws the rightantennae
        self.catipillar_turtle.setheading(55)
        self.catipillar_turtle.forward(size)
        self.catipillar_turtle.pendown()
        self.catipillar_turtle.forward(size)

    def draw_legs(self,size,color):
        #Changes color of the fill
        self.catipillar_turtle.color(color,color)
        self.catipillar_turtle.penup()
        for x in range(4):
            #Goves to the left leg position, moving up each time it loops
            self.catipillar_turtle.goto(-size,(x-3/2)*size)
            self.catipillar_turtle.pendown()
            #draws the left leg
            self.catipillar_turtle.goto(self.catipillar_turtle.xcor()-size,self.catipillar_turtle.ycor())
            self.catipillar_turtle.goto(self.catipillar_turtle.xcor()-size,self.catipillar_turtle.ycor()-size/2)
            self.catipillar_turtle.penup()
            #goes to where the right leg starts
            self.catipillar_turtle.goto(size,self.catipillar_turtle.ycor()+size/2)
            self.catipillar_turtle.pendown()
            #draws the right leg
            self.catipillar_turtle.goto(self.catipillar_turtle.xcor()+size,self.catipillar_turtle.ycor())
            self.catipillar_turtle.goto(self.catipillar_turtle.xcor()+size,self.catipillar_turtle.ycor()-size/2)
            self.catipillar_turtle.penup()

    def display(self):
        #Draws each part of the Caterpillar
        self.draw_body(self.body_size,self.body_color)
        self.draw_antennae(self.body_size,self.leg_color)
        self.draw_legs(self.body_size,self.leg_color)
        turtle.done()
