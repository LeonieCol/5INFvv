import random

getal = random.randint(1, 100)

while True:
    gok = input("Raad het geheime getal tussen 1 en 100 (of 'q' om te stoppen): ")

    if gok.lower() == "q":
        break

    try:
        gok = int(gok)
    except ValueError:
        print("Voer een getal in of typ 'q' om te stoppen.")
        continue

    if gok == getal:
        print("Gefeliciteerd, je hebt het getal geraden!")
        break
    else:
        print("Helaas, dat is niet correct. Probeer het nog eens.")
    
