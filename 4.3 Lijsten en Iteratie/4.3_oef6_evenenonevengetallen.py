getallen = list(range(1,21))

even_getallen = [] 
oneven_getallen = []

for getal in getallen: 
    if getal % 2 == 0:
        even_getallen.append(getal) 
    else: 
        oneven_getallen.append(getal)

print("Even getallen: ", even_getallen)
print("Oneven getallen:", oneven_getallen)
