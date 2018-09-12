import turtle
import random
turtle.speed(100)

while((abs(turtle.xcor())<475) or (abs(turtle.ycor())<400)):
    heading = (random.randint(1,4)-1)*90
    turtle.right(heading)
    turtle.forward(20)
turtle.done()
