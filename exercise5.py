counter = 1
validator = []
l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
while True:
    for i in l:
        if counter % i == 0:
            validator.append(True)
    if len(validator) == len(l):
        break
    else:
        validator = []
        counter += 1

print(counter)