zin = input("Voer een zin in: ")
woorden = zin.lower().split()
woord_frequentie = {}

for woord in woorden:
    if woord in woord_frequentie:
        woord_frequentie[woord] += 1
    else:
        woord_frequentie[woord] = 1

print("Woordfrequentie:")
for woord, aantal in woord_frequentie.items():
    print(f"{woord}: {aantal}")