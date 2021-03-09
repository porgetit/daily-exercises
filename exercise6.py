sumA = 0
for i in range(1,101):
    sumA += i**2
print("La suma de los cuadrados es:", sumA)

sumB = 0
for i in range(1,101):
    sumB += i
sumB **= 2
print("El cuadrado de la suma es:", str(sumB))

print("La diferencia es:", str(sumB-sumA))