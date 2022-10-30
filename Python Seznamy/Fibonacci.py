konechod = int(input("Zadejte koncovou hodnotu."))

x = 0
y = 1
while y <= konechod:
    print(x, " ", end="")
    print(y, " ", end="")
    x=x+y
    y=y+x
if x<=konechod:
    print(x)

#rada zacina od 1