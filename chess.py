import turtle

# Set up the turtle window
screen = turtle.Screen()
screen.setup(1000, 1000)
screen.title("Chessboard")

# Set up the turtle
turtle.speed(0)
turtle.hideturtle()

# Define the size of the squares
square_size = 50

# Draw the chessboard
for row in range(8):
    for col in range(8):
        if (row + col) % 2 == 0:
            turtle.fillcolor("white")
        else:
            turtle.fillcolor("black")
        turtle.penup()
        turtle.goto(col * square_size, row * square_size)
        turtle.pendown()
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(square_size)
            turtle.right(90)
        turtle.end_fill()

# Keep the turtle window open
turtle.done()
