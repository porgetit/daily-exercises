dict = {}
for i in range(100, 1000):
    for j in range(100, 1000):
        key = f"{i} * {j}"
        value = i*j 
        dict[key] = value

list = []
for i in dict:
    string = str(dict[i])
    if string != string[::-1]:
        list.append(i)

print("Len List:",len(list))
print("Len Dict:",len(dict))

for i in list:
    dict.pop(i)

print("Len Dict:",len(dict))
print(max(dict.values()))