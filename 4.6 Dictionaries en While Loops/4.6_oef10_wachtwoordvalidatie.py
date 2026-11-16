speciale_tekens = "!@#$%^&*"

while True:
    print(" - Minimaal 8 karkakters lang")
    print(" - Bevat ten minste 1 hoofdletter")
    print(" - Bevat ten minste 1 cijfer")
    print(" - Bevat ten minste 1 speciaal karakter (bijv. !@#$%^&*)")
    print()
    wachtwoord = input("Geef een wachtwoord in dat aan de bovenstaande criteria voldoet: ")

    if len(wachtwoord) < 8: 
        print("Je wachtwoord is te kort, probeer het opnieuw.")

    if not any ([teken.isupper() for teken in wachtwoord]):
        print("Er moet minstens 1 hoofdletter in je wachtwoord staan, probeer het opnieuw.")

    if not any ([teken.isdigit() for teken in wachtwoord]):
        print("Er moet minstens 1 cijfer in je wachtwoord staan, probeer het opnieuw.")

    if not any(teken in speciale_tekens for teken in wachtwoord):
        print("Er moet minstens 1 speciaal teken in je wachtwoord staan, probeer het opnieuw.")
        
    if True: 
        print("Bedankt om de criteria te respecteren :)")

    else:
        break

    