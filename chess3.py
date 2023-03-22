import turtle

# Set up the turtle window
screen = turtle.Screen()
screen.setup(500, 500)
screen.title("Chessboard")

# Set up the turtle
turtle.speed(0)
turtle.hideturtle()

# Define the size of the squaresimport turtle

# Set up the turtle window
screen = turtle.Screen()
screen.setup(400, 400)
screen.title("Chessboard")

# Set up the turtle
turtle.speed(0)
turtle.hideturtle()

# Define the size of the squares
def get_square_size():
    window_width = screen.window_width()
    square_size = window_width / 8
    return square_size

square_size = get_square_size()

# Draw the chessboard
for row in range(8):
    for col in range(8):
        if (row + col) % 2 == 0:
            turtle.fillcolor("white")
        else:
            turtle.fillcolor("black")
        turtle.penup()
        turtle.goto(col * square_size - screen.window_width() / 2, row * square_size - screen.window_height() / 2)
        turtle.pendown()
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(square_size)
            turtle.right(90)
        turtle.end_fill()

# Keep the turtle window open
turtle.done()

window_size = screen.window_width()
square_size = window_size / 8

# Draw the chessboard
for row in range(8):
    for col in range(8):
        if (row + col) % 2 == 0:
            turtle.fillcolor("white")
        else:
            turtle.fillcolor("black")
        turtle.penup()
        turtle.goto(col * square_size - window_size / 2, row * square_size - window_size / 2)
        turtle.pendown()
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(square_size)
            turtle.right(90)
        turtle.end_fill()

# Keep the turtle window open
turtle.done()
