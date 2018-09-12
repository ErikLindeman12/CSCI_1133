def main():
    import turtle
    x = 0
    turtleInt = turtle.numinput("Number", "Your Number",36, minval = 1,maxval = 360)
    number = 360/turtleInt

    while(x<=360):
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.left(number)
        x+=number
    turtle.done()

if  __name__  == '__main__':
    main()
