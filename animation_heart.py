import turtle
import math
import random


def xt(t):
    return 16 * math.sin(t) ** 3


def yt(t):
    return 13 * math.cos(t) - 5 \
        * math.cos(2 * t) - 2 * \
        math.cos(3 * t) - math.cos(4 * t)


t = turtle.Turtle()
turtle.title("МОЕМУ МАЛЕНЬКОМУ МАЛЫШУ")
t.speed(500)
turtle.colormode(255)
turtle.Screen().bgcolor(0, 0, 0)
colors = ["120,81,169", "138,43,226",
          "153,50,204", "148,0,211", "102,0,153"
          ]
for i in range(2550):
    t.goto((xt(i) * 20, yt(i) * 20))
    #    t.pencolor((255 - i) % 255, i % 255, (255 + i) // 2 % 255)
    t.pencolor([int(x) for x in colors[random.randint(0, len(colors) - 1)].split(",")])
    t.goto(0, 0)

t.hideturtle()
turtle.update()
turtle.mainloop()
