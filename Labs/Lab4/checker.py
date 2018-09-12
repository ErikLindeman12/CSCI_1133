import turtle
x = turtle.window_width()
turtle.speed(100)
row = 1
column = 1
time=1
turtle.setup(width = x, height = x,startx=0, starty=0)
def drawSquare(row,column,time):
    turtle.penup()
    turtle.goto(-x/2+(x/8)*(row-1),x/2-(column)*(x/8))
    turtle.pendown()
    if(time%2==1):
        turtle.color('red')
    else:
        turtle.color('black')
    turtle.begin_fill()
    turtle.forward(x/8)
    turtle.left(90)
    turtle.forward(x/8)
    turtle.left(90)
    turtle.forward(x/8)
    turtle.left(90)
    turtle.forward(x/8)
    turtle.left(90)
    turtle.end_fill()
while(column<=8):
    while(row<=8):
        drawSquare(row,column,time)
        row+=1
        time+=1
    column+=1
    row=1
    time+=1
turtle.hideturtle()
turtle.done()
