# Los factores primos de 13195 son 5, 7, 13 y 29. ¿Cuál es el factor primo más grande del número 600851475143?

def primos():
    prs = []
    lista = 100
    cont = 0
    for i in range(2, lista + 1):
        primos = True
        for j in range(2,11):
            if i == j:
                break
            elif i%j == 0:
                primos = False
            else:
                continue
        if primos == True:
            prs.append(i)
            cont += 1
    return prs

num = int(input("Número: "))
list_primes = primos()
counter = 0
item = 0
index = 0


while True:
    item = list_primes[index]
    if num % item == 0:
        counter += 1
        num /= item
        print("factor", counter, ":", str(item))
    elif item > len(list_primes)-1 :
        break
    elif item < 2:
        break
    else:
        index += 1