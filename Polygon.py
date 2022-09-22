import turtle

strany = int(input("Zadejte pocet stran: "))
delka = int(input("Zadejte delku:"))
uhel = 360/strany

t = turtle.Turtle()

for i in range(strany):
    t.forward(delka)
    t.left(uhel)
