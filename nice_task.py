import turtle

cursor = turtle.Turtle()


def draw_dick():
    for i in range(4):
        cursor.forward(50)
        cursor.left(90)

    cursor.right(180)
    for i in range(3):
        cursor.forward(50)
        cursor.right(90)
    cursor.right(90)
    cursor.forward(25)
    cursor.right(90)
    cursor.fd(300)
    cursor.right(90)
    cursor.fd(50)
    cursor.right(90)
    cursor.fd(300)


def drawing_circle():
    turtle.bgcolor("black")
    cursor.pencolor("violet")
    right_angle = 90
    angle = 90
    for k in range(50):
        for i in range(4):
            cursor.right(angle)
            cursor.circle(100)
            cursor.right(right_angle - angle)
        angle /= 2


drawing_circle()

turtle.done()
