lichcislo = int(input("Zadej liche číslo"))

if lichcislo % 2 == 0:
    lichcislo += 1

list = [lichcislo]

for i in range(9):
    lichcislo += 2
    list.append(lichcislo)
print(list)
