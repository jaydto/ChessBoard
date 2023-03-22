import turtle

# Set up the turtle window
screen = turtle.Screen()
screen.setup(500, 500)
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

# Set up the pieces on the board
pieces = {}

# Black pieces
pieces["b_rook1"] = turtle.Turtle()
pieces["b_rook1"].penup()
pieces["b_rook1"].goto(-3.5 * square_size, -3.5 * square_size)
pieces["b_rook1"].shape("square")
pieces["b_rook1"].color("black")
pieces["b_rook1"].shapesize(2, 2)

pieces["b_knight1"] = turtle.Turtle()
pieces["b_knight1"].penup()
pieces["b_knight1"].goto(-2.5 * square_size, -3.5 * square_size)
pieces["b_knight1"].shape("circle")
pieces["b_knight1"].color("black")
pieces["b_knight1"].shapesize(2, 2)

