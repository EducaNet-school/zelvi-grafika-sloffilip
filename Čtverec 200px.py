import turtle

t = turtle.Turtle()

for i in range(4):
    t.forward(100)
    t.left(90)

t.penup()
t.goto(-200,0)
t.pendown()

for i in range(4):
    t.forward(100)
    t.left(90)
