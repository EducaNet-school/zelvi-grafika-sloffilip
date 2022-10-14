start = int(input("Jaké bude počáteční číslo?"))
end = int(input("Jaké bude konečné?"))

if start<end:
    for num in range(start, end + 1):
        if num % 2 != 0:
            print(num, end = " ")

else:
    print("Jak může být konečné číslo větší než počáteční?")
