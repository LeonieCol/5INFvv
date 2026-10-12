zin = input("Voer een zin in: ").lower()

woorden_lijst = zin.split()

unieke_woorden = []
frequenties = []

for woord in woorden_lijst:
    if woord not in unieke_woorden:
        unieke_woorden.append(woord)

for uniek in unieke_woorden:
    teller = 0
    for woord in woorden_lijst:
        if woord == uniek:
            teller = teller + 1
    print (f"{uniek}: {teller}")