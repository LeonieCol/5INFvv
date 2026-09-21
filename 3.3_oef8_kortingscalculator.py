bedrag = float(input("Voer het aankoopbedrag in: "))

if bedrag > 100: 
    korting_percentage = 10
else:
    if bedrag > 50: 
        korting_percentage = 5
    else:
        korting_percentage = 0

korting_bedrag = bedrag * (korting_percentage / 100)
eindprijs = bedrag - korting_bedrag

if korting_percentage > 0: 
    print(f"Je krijgt {korting_percentage}% korting.")
else:
    print("Je krijgt geen korting.")

print(f"De uitendelijke prijs is: €{eindprijs}")