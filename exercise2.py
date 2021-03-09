# Cada nuevo termino en la sucesión de Fibonacci se genera sumando los dos términos previos.
# Si comenzamos con 1 y 2, los primeros 10 términos serán: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Si consideramos los términos de la sucesión de Fibonacci cuyos valores no excedan los 4 millones, determine la suma de todos los valores pares.

list = [1, 2,]

for i in range(2, 32):
    list.append(list[i-1] + list[i-2])

fibonacci_list = list
sum = 0

for i in fibonacci_list:
    if i % 2 == 0:
        sum += i

print(fibonacci_list)
print("suma:", sum)

# [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578]
# suma: 4613732