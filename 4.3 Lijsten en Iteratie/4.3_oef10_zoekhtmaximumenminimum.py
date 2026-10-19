import random

lijst = [] 
for i in range(10):
    lijst.append(random.randint(1,100))

print(lijst)

minimum = lijst[0]
maximum = lijst[0]

for getal in lijst: 
    if getal < minimum:
        minimum = getal
    if getal > maximum:
        maximum = getal

print(f"Maximum = {maximum}")
print(f"Minimum = {minimum}")
