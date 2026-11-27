# Startgegevens klaarzetten
aandelen = {
    "TechNova":   {"aantal": 10, "koersen": [52.10, 53.40, 51.80, 54.90, 56.20, 55.70]},
    "GreenPower": {"aantal": 25, "koersen": [18.30, 18.10, 17.60, 17.90, 17.20, 16.80]},
    "FoodCorp":   {"aantal": 15, "koersen": [33.00, 33.50, 33.20, 34.10, 34.00, 34.60]},
}
cash = 500.0
transactiekost = 2.50

# 1. Per aandeel de gemiddelde, hoogste en laagste koers tonen: 

# We doorlopen de dictionary met een for-lus, zodat we geen aparte variabelen per aandeel hoeven te maken. 
for naam in aandelen: #Voorbeeld ronde 1: naam = "TechNova"
    koersen = aandelen[naam]["koersen"]  # Haalt de lijst[52.10, 53.40, 51.80, 54.90, 56.20, 55.70].

    # Startwaarden klaarzetten voor dit aandeel: we starten bij de eerste koers (index 0) om mee te kunnen vergelijken
    totaal = 0
    hoogste = koersen[0] 
    laagste = koersen[0]

    # Elk getal in de lijst 'koersen' één voor één bekijken
    for koers in koersen: 
        totaal = totaal + koers      # Alle koersen optellen voor het gemiddelde
        if koers > hoogste:          # Is deze koers hoger dan het huidige record? 
            hoogste = koers 
        if koers < laagste:          # Is deze koers lager dan het huidige laagsterecord?
            laagste = koers

    gemiddelde = totaal / len(koersen)

    # Resultaat tonen met 2 decimalen (verplichte bouwsteen: f-string)
    print(f"{naam}: gemiddelde = {gemiddelde:.2f}, hoogste = {hoogste:.2f}, laagste = {laagste:.2f}")
   

# 2. Het rendement in % tussen de eerste en de laatste dag berekenen, en het beste en slechtste aandeel tonen. 

# Startwaarden klaarzetten om het beste en slechtste aandeel te onthouden.
# We kiezen extreme startgetallen (-999999 en 999999), zodat zelfs als alle aandelen verlies maekn (negatief %), het eerste aandeel toch wint. 
beste_aandeel = ""
beste_rendement = -999999
slechtste_aandeel = ""
slechtste_rendement = 999999

# We doorlopen de dictionary een keer per aandeel
for naam in aandelen: 
    koersen = aandelen[naam]["koersen"]

    # Eerste en allerlaatste koers uit de lijs halen (index 0 = eerste, index -1 = laastste)
    eerste_dag = koersen[0]
    laatste_dag = koersen[-1]

    # Formule voor procentueel rendement: ((nieuw - oud) / oud) * 100
    rendement = ((laatste_dag - eerste_dag)/eerste_dag)*100
    print(f"{naam}: rendement = {rendement:.2f}%")

    # Controleren of dit aandeel een hoger rendement heeft dan het huidige beste aandeel
    if rendement > beste_rendement:
        beste_rendement = rendement  # Nieuw hoogste percentage opslaan
        beste_aandeel = naam         # De naam van dit aandeel onthouden

    # Controleren of dit aandeel een lager rendement heeft dan het huidige slechtste aandeel
    if rendement < slechtste_rendement:
        slechtste_rendement = rendement  # Nieuw laagste percentage opslaan
        slechtste_aandeel = naam         # De naam van dit aandeel opslaan 

# Pas NADAT de lus alle aandelen heeft vergeleken (helemaal links uitgelijnd!), tonen we de winnaar en verliezer: 
print(f"Beste aandeel: {beste_aandeel}{beste_rendement:.2f}%")
print(f"Slechtste aandeel: {slechtste_aandeel}{slechtste_rendement:.2f}%")

# 3. De totale waarde van de portefeuille en het aandeel in % van elk aandeel tonen.

# Deel 1: Totale waarde berekenen (we starten meteen met het cashgeld op onze rekening)
totale_waarde = cash

# We lopen één keer door alle aandelen in de dictionary
for naam in aandelen:
    stuks = aandelen[naam]["aantal"]             # Aantal stuks van dit aandeel (is een gewoon getal, dus geen lus nodig!)
    laatste_koers = aandelen[naam]["koersen"][-1] # De meest recente koers van dit aandeel
    
    # Waarde van dit specifieke aandeel berekenen en optellen bij het totaal
    waarde_aandeel = stuks * laatste_koers
    totale_waarde = totale_waarde + waarde_aandeel

# Pas ná de lus is alles opgeteld en printen we de totale waarde (met 2 decimalen)
print(f"Totale waarde van de portefeuille: €{totale_waarde:.2f}")

# Deel 2: Nu we het totaal kennen, berekenen we voor elk aandeel hoeveel % dit is van de totale portefeuille
for naam in aandelen:
    stuks = aandelen[naam]["aantal"]
    laatste_koers = aandelen[naam]["koersen"][-1]
    waarde_aandeel = stuks * laatste_koers

    # Formule: (deel / geheel) * 100
    percentage = (waarde_aandeel / totale_waarde) * 100
    print(f"- {naam}: {percentage:.2f}% van de totale waarde")

# 4. Aandel kopen of verkopen aan de laatste koers, met transactiekost;
# je kan niet meer kopen dan je chash toelaat en niet meer verkopen dan je bezit. 

# Deze functie regelt het kopen en het verkopen van aandelen en geeft het nieuwe cashsaldo terug.
def verhandel_aandelen(aandelen, cash, transactiekost):
    """Laat de gebruiker aandelen kopen of verkopen aan de laatste slotkoers en geeft het bijgewerkte cashsaldo terug."""

    # We vragen of de gebruiker wil kopen of verkpoen
    actie = input("Wil je aandelen kopen of verkopen? (typ hier 'kopen' of 'verkopen'): ").lower()

    # Eerst controlern of de invoer wel geldig
    if actie != 'kopen' and actie != 'verkopen':
        print("Ongeldige keuze. Kies 'kopen' of 'verkopen': ")
        return cash # We stoppen de functie en geven het ongewijzigde cashsaldo terug

    # We vragen om welk aandeel het gaat en controleren of het bestaat in de dictionary
    gekozen_aandeel = input("Welk aandeel wil je verhandelen? (TechNova, GreenPower, FoodCorp): ")
    if gekozen_aandeel not in aandelen: 
        print("Four: dit aandeel bestaat niet in je portefeuille.")
        return cash
