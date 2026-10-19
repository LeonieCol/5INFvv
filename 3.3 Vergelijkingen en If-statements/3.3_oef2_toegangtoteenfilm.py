leeftijd = int(input("Wat is je leeftijd? "))
begeleid = input("Ben je met een volwassene? (ja/nee): ").lower()

if leeftijd >= 16 or begeleid == "ja":
    print("Je mag naar de film.")
else:
    print("Sorry, je mag niet naar de film.")