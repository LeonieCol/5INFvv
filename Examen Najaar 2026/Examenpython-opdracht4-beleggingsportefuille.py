#Startgegevens klaarzetten
aandelen = {
    "TechNova":   {"aantal": 10, "koersen": [52.10, 53.40, 51.80, 54.90, 56.20, 55.70]},
    "GreenPower": {"aantal": 25, "koersen": [18.30, 18.10, 17.60, 17.90, 17.20, 16.80]},
    "FoodCorp":   {"aantal": 15, "koersen": [33.00, 33.50, 33.20, 34.10, 34.00, 34.60]},
}
cash = 500.0
transactiekost = 2.50

# 1. Per aandeel de gemiddelde, hoogste en laagste koers tonen: 

#We doorlopen de dictionary met een for-lus, zodat we geen aparte variabelen per aandeel hoeven te maken. 
for naam in aandelen: #Voorbeeld ronde 1: naam = "TechNova"
    koersen = aandelen[naam]["koersen"]  #Haalt de lijst[52.10, 53.40, 51.80, 54.90, 56.20, 55.70].

    #Startwaarden klaarzetten voor dit aandeel: we starten bij de eerste koers (index 0) om mee te kunnen vergelijken
    totaal = 0
    hoogste = koersen[0] 
    laagste = koersen[0]

    #Elk getal in de lijst 'koersen' één voor één bekijken
    for koers in koersen: 
        totaal = totaal + koers      #Alle koersen optellen voor het gemiddelde
        if koers > hoogste:          #Is deze koers hoger dan het huidige record? 
            hoogste = koers
        if koers < laagste:          #Is deze koers lager dan het huidige laagsterecord?
            laagste = koers

    gemiddelde = totaal / len(koersen)

    #Resultaat tonen met 2 decimalen (verplichte bouwsteen: f-string)
    print(f"{naam}: gemiddelde = {gemiddelde:.2f}, hoogste = {hoogste:.2f}, laagste = {laagste:.2f}")

# 2. Het rendement in % tussen de eerste en de laatste dag berekenen, en het beste en slechtste aandeel tonen. 

#We nemen weer de dictionary door:
for naam in aandelen: 
    koersen = aandelen[naam]["koersen"]

    #Startwaarde klaarzetten: 
    eerste_dag = koersen[0]
    laatste_dag = koersen[-1]

    #Rendement formule gebruiken voor elk getal in de lijst koersen
    rendement = ((laatste_dag - eerste_dag)/eerste_dag)*100

    print(f"{naam}: rendement = {rendement:.2f}%")