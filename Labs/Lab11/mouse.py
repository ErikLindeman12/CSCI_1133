import turtle

def mouseInput(x,y):
  print(x,',',y)

this = turtle.Turtle()
scr = this.getscreen()
scr.onclick(mouseInput)
scr.listen()
