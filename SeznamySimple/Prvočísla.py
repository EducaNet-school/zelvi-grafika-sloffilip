sez = []

def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True


    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True


def printPrime(n):
    for i in range(2, n + 1):
        if isPrime(i):
            print (i, end =" ")

n = int(input("Jaké číslo bude končit?"))
printPrime(n)

#pekne pouziti funkci, neukladas do seznamu


