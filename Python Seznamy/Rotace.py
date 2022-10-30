l1 = [1,2,3,4]
print("Původní seznam: " + str(l1))

otazka = int(input("O kolik chcete seznam posunout?"))
otazka2 = input("A jakým směrem?")

if otazka == 1 and otazka2 == "Doleva":
    l1 = l1[1:] + l1[:1]
    print("Levá rotace seznamu o 1 : " + str(l1))

if otazka == 1 and otazka2 == "Doprava":
    l1 = l1[-1:] + l1[:-1]
    print("Pravá rotace seznamu o 1 : " + str(l1))

if otazka == 2 and otazka2 == "Doprava":
    l1 = l1[2:] + l1[:2]
    print("Pravá rotace seznamu o 2 : " + str(l1))


if otazka == 2 and otazka2 == "Doleva":
    l1 = l1[-2:] + l1[:-2]
    print("Levá rotace seznamu o 2 : " + str(l1))

# je to velmi tezkopadne, kdyby mel seznam 1000 polozek, tak se
# hodne napracujes