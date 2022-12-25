# import turtle
# import math
#
#
# def xt(t):
#     return 16 * math.sin(t) ** 3
#
#
# def yt(t):
#     return 13 * math.cos(t) - 5 \
#         * math.cos(2 * t) - 2 * \
#         math.cos(3 * t) - math.cos(4 * t)
#
#
# t = turtle.Turtle()
# t.speed(500)
# turtle.colormode(255)
# turtle.Screen().bgcolor(0, 0, 0)
# for i in range(2550):
#     t.goto((xt(i) * 20, yt(i) * 20))
#     t.pencolor((255 - i) % 255, i % 255, (255 + i) // 2 % 255)
#     t.goto(0, 0)
# t.hideturtle()
# turtle.update()
# turtle.mainloop()

import turtle

# Creating a turtle object(pen)
pen = turtle.Turtle()


# Defining a method to draw curve
def curve():
    for i in range(200):
        # Defining step by step curve motion
        pen.right(1)
        pen.forward(1)


# Defining method to draw a full heart
def heart():
    # Set the fill color to red
    pen.fillcolor('red')

    # Start filling the color
    pen.begin_fill()

    # Draw the left line
    pen.left(140)
    pen.forward(113)

    # Draw the left curve
    curve()
    pen.left(120)

    # Draw the right curve
    curve()

    # Draw the right line
    pen.forward(112)

    # Ending the filling of the color
    pen.end_fill()


# Defining method to write text
def txt():
    # Move turtle to air
    pen.up()

    # Move turtle to a given position
    pen.setpos(-68, 95)

    # Move the turtle to the ground
    pen.down()

    # Set the text color to lightgreen
    pen.color('lightgreen')

    # Write the specified text in
    # specified font style and size
    pen.write("GeeksForGeeks", font=(
        "Verdana", 12, "bold"))


# Draw a heart
heart()

# Write text
txt()

# To hide turtle
pen.ht()