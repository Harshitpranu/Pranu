from turtle import *
t = Turtle()
s = Screen()
s.bgcolor("black")
t.pencolor("red")

a = 0
b = 0
t.speed(0)
t.penup()
t.goto(0, 200)
t.pendown()
while (True):
    t.forward(a)
    t.right(b)
    a=a+3
    b=b+1
    if b == 210:
        break
    t.hideturtle()

done()