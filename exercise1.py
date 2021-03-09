# Si obtenemos los números enteros inferiores a 10 múltiplos de 3 y de 5 en una lista. 
# Tendremos el siguiente resultado: [3,5,6,9]. 
# La suma de todos estos múltiplos es 23. 
# Así mismo, obtenga la suma de todos los múltiplos de 3 y de 5 inferiores a 1000.

list_of_numbers = range(1, 1000)

list_items = []

for i in list_of_numbers:
    if i % 3 == 0 or i % 5 == 0:
        list_items.append(i)
    
print(list_items)

sum = 0
for i in list_items:
    sum += i

print("La suma de todos los dígitos es:", sum)