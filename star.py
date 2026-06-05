import turtle
turtle.Screen().bgcolor("Orange")
s=turtle.Screen()
s.setup(500,500)
turtle.title("Welcome to turtle window")
board=turtle.Turtle()
for i in range(5):
    board.forward(144)
    board.right(144)
    i=i+1
turtle.done()