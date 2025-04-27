#Marco Campos
#April 6, 2025
#P4 LAb 1B
#Using turtle to draw initials

import turtle

# Set up turtle
t = turtle.Turtle()
t.pensize(5)
t.color("green")

# Draw "M"
t.penup()
t.goto(-100, 0)
t.pendown()
t.left(90)
t.forward(100)         # Left vertical line
t.right(135)
t.forward(50 * (2**0.5))  # Diagonal to middle
t.left(90)
t.forward(50 * (2**0.5))  # Diagonal to right top
t.right(135)
t.forward(100)         # Right vertical line

# Move to draw "C"
t.penup()
t.goto(50, 100)
t.setheading(180)
t.pendown()
t.circle(50, 180)      # Draw half-circle for C

# Finish
t.hideturtle()
turtle.done()
