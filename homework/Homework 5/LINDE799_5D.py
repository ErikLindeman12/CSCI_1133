#CSCI 1133 Homework 5
#Erik Lindeman
#5D

def squares(t,length,depth):
    xcor = t.xcor()
    ycor = t.ycor()
    t.penup()
    t.goto(xcor+length/2,ycor+length/2)
    t.pendown()
    t.goto(xcor-length/2,ycor+length/2)
    t.goto(xcor-length/2,ycor-length/2)
    t.goto(xcor+length/2,ycor-length/2)
    t.goto(xcor+length/2,ycor+length/2)
    t.penup()
    t.goto(xcor,ycor)
    if(depth>1):
        t.goto(xcor+(3/4*length),ycor)
        squares(t,length/2,depth-1)
        t.goto(xcor-(3/4*length),ycor)
        squares(t,length/2,depth-1)
        t.goto(xcor,ycor+(3/4*length))
        squares(t,length/2,depth-1)
        t.goto(xcor,ycor-(3/4*length))
        squares(t,length/2,depth-1)

def main():
    depth = int(input("What would you like the initial depth to be? "))
    import turtle
    t = turtle.Turtle()
    t.speed(0)
    squares(t,200,depth)
    t.hideturtle()
    turtle.done()

if  __name__  == '__main__':
    main()
