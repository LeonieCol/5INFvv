telefoonboek = {}
afgesloten = False

for beurt in range(100):
    if not afgesloten:
        print("Telefoonboek menu")
        print("1. Contact toevoegen")
        print("2. Contact opzoeken")
        print("3. Contact verwijderen")
        print("4. Alle contacten weergeven")
        print("5. Afsluiten")
        keuze = input("Kies een optie: ")
        print ()

        if keuze == "1":
            naam = input("Naam: ").lower()
            if naam in telefoonboek:
                print(f"Sorry, {naam} staat al in telefoonboek.")
            else: 
                nummer = input("Telefoonnummer: ")
                telefoonboek[naam] = nummer
                print("Contact toegevoegd")
            
        elif keuze == "2":
            naam = input("Welk contact wil je opzoeken?").lower()
            if naam in telefoonboek:
                print(f"{naam}: {telefoonboek[naam]}")
            else:
                print("Contact niet gevonden.")

        elif keuze == "3":
            
            naam = input("Welk contact wil je verwijderen?").lower()
            if naam in telefoonboek: 
                del telefoonboek[naam]
                print(f"{naam} is uit je telefoonboek verwijderd.")
            else: 
                print("Dit contact staat niet in het telefoonboek.")
        
        elif keuze == "4": 
            if telefoonboek:
                print("Alle contacten:")
                for naam, nummer in telefoonboek.items():
                    print(f"- {naam}: {nummer}")
            else: 
                print("Het telefoonboek is nog leeg.")

        elif keuze == "5": 
            print("Tot ziens")
            afgesloten = True

        else: 
            print("Je hebt een ongeldige keuze ingegeven, geef een cijfer van 1 t.e.m. 5 in.")

