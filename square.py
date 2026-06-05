import turtle
turtle.Screen().bgcolor("Orange")
s=turtle.Screen()
s.setup(500,500)
turtle.title("Welcome to turtle window")
board=turtle.Turtle()
for i in range(4):
    board.forward(100)
    board.right(90)
    i=i+1
turtle.done()