num = int(input("Zadejte číslo malé násobilky (1-10)"))

if num < 11 and num >=2:
    for i in range(1, 11):
        print(num, 'x', i, '=', num*i)

else:
    print("Říkám ti malou násobilku!")

#pekny format print, dobra kontrola uzivatelskeho vstupu
#neukladas do seznamu