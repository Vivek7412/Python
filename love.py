import math
import turtle
def xt(t):
    return 16*math.sin(t)**3
def yt(t):
    return 13*math.cos(t)-5*\
        math.cos(2*t)-2*\
            math.cos(3*t)-\
                math.cos(4*t)
t = turtle.Turtle()
t.speed(400)
turtle.bgcolor('black')

for i in range(1500):
    t.goto((xt(i)*15,yt(i)*15))
    t.pencolor('red')
    t.goto(0,0)
    