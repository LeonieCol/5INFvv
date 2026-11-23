def filter_even_getallen(getallen):

    even_getallen = [] 
    oneven_getallen = []

    for getal in getallen: 
        if getal % 2 == 0:
            even_getallen.append(getal) 
        else: 
            oneven_getallen.append(getal)

    return even_getallen

getallen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_even_getallen(getallen))
