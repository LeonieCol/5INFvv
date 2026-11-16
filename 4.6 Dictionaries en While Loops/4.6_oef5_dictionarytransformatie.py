producten = {
    "appel": 0.75,
    "banaan": 1.20,
    "sinaasappel": 1.50,
    "kiwi": 2.00,
    "druiven": 2.50,
    "mango": 1.95,
    "ananas": 3.25
}

prijzen_verhoogd = {}
for product, prijs in producten.items():
    prijzen_verhoogd[product] = round(prijs * 1.05, 2)

print("Prijzen met 5% verhoogd:")
print(prijzen_verhoogd)
print()


duurder_dan_1_50 = {}
for product, prijs in producten.items():
    if prijs > 1.50:
        duurder_dan_1_50[product] = prijs

print("Producten duurder dan € 1.50:")
print(duurder_dan_1_50)
print()


hoofdletters_producten = {}
for product, prijs in producten.items():
    hoofdletters_producten[product.upper()] = prijs

print("Sleutels in hoofdletters:")
print(hoofdletters_producten)
