import turtle

t = turtle.Turtle()
delka = 0
umisteni1 = 0
umisteni2 = 0
while True:
    t.speed(100)
    t.penup()
    t.goto(umisteni1, umisteni2)
    t.pendown()
    delka += 4
    umisteni1 -= 2
    umisteni2 -= 2
    for i in range(4):
      t.forward(delka)
      t.left(90)
