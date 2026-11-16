woordenboek = {
    "hallo": {"Engels": "hello", "Frans": "bonjour", "Duits": "hallo"},
    "wereld": {"Engels": "world", "Frans": "monde", "Duits": "welt"},
}

woord = input("Voer een Nederlands woord in: ").lower().strip()
taal = input("Kies een doeltaal (Engels, Frans, Duits): ").strip().lower().capitalize()
print(taal)
if woord in woordenboek: 
    if taal in woordenboek[woord]:
        vertaling = woordenboek[woord][taal]
        print(vertaling)
    else: 
        print('Taal niet juist')

else:
    print("Woord staat niet in woordenboek")
