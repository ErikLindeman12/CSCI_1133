#CSCI 1133 Homework 5
#Erik Lindeman
#5 Bonus

def triangles(t,length,depth):
    xcor = t.xcor()
    ycor = t.ycor()
    t.goto(xcor-length/2,ycor)
    t.right(60)
    t.forward(length)
    t.left(120)
    t.forward(length)
    t.left(120)
    t.forward(length)
    t.left(60)
    t.forward(length)
    t.left(120)
    t.forward(2*length)
    t.left(120)
    t.forward(2*length)
    t.left(120)
    t.forward(length)
    t.setheading(0)
    t.goto(xcor,ycor)
    otherLength = ((3**(1/2))/2)*length/2
    if(depth>1):
        t.penup()
        t.goto(xcor,ycor+otherLength)
        t.pendown()
        triangles(t,length/2,depth-1)
        t.penup()
        t.goto(xcor+length/2,ycor-otherLength)
        t.pendown()
        triangles(t,length/2,depth-1)
        t.penup()
        t.goto(xcor-length/2,ycor-otherLength)
        t.pendown()
        triangles(t,length/2,depth-1)

def main():
    depth = int(input("What would you like the initial depth to be? "))
    import turtle
    t = turtle.Turtle()
    t.speed(0)
    triangles(t,200,depth)
    t.hideturtle()
    turtle.done()

if  __name__  == '__main__':
    main()
