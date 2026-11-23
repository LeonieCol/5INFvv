#Start gegevens importeren:
aandelen = {
    "TechNova":   {"aantal": 10, "koersen": [52.10, 53.40, 51.80, 54.90, 56.20, 55.70]},
    "GreenPower": {"aantal": 25, "koersen": [18.30, 18.10, 17.60, 17.90, 17.20, 16.80]},
    "FoodCorp":   {"aantal": 15, "koersen": [33.00, 33.50, 33.20, 34.10, 34.00, 34.60]},
}
cash = 500.0
transactiekost = 2.50

#1. Per aandeel de gemiddelde, hoogste en laagste koers tonen: 

#Eerst moeten we de koersen appart kunnen bijkijken om deze dingen te berekenen, om dit te doen maken we geen apparte variabele voor ieder aandeel, maar gaan we automatisch een for-lus gebruiken die de dictionary doorloopt. 
for naam in aandelen: #RONDE 1 ALS VOORBEELD:
    koersen = aandelen[naam]["koersen"]  #Naam = 'TechNova', de variabele wordt dus automatisch [52.10, 53.40, 51.80, 54.90, 56.20, 55.70].
    print(naam, koersen)
