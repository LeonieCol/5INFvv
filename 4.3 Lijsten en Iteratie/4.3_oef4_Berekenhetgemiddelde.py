#Vraag aan de gebruiker hoeveel getallen er komen
aantal_getallen = int(input("Hoeveel getallen wil je invoeren? "))

#Maak een lege lijst om de getallen in te bewaren 
getallen_lijst = []

#Gebruik een range-lus om herhaaldelijk om een getaln te vragen
for i in range(1, aantal_getallen +1): 
    getal = float(input(f"Voer getal {i} in: "))
    getallen_lijst.append(getal) #Voeg het getal toe aan de lijst
    
#Bereken de som van de getallen in de lijst
totale_som = 0
for getal in getallen_lijst:
    totale_som  = totale_som + getal

#Bereken het gemiddelde
gemiddelde = totale_som / aantal_getallen

#Print het resultaat netjes afgerond op 2 decimalen
print(f"Het gemiddelde is: {gemiddelde:.2f}")
