#Vaste wisselkoers: 1 EUR = 1.15 USD op 18/09/2026
WISSELKOERS_EUR_NAAR_USD = 1.15

bedrag = float(input("Bedrag: "))
bronvaluta = input("Bronvaluta (EUR of USD): ").strip().upper()

if bronvaluta == "EUR" : 
    doelvaluta = "USD"
    resultaat = bedrag * WISSELKOERS_EUR_NAAR_USD
elif bronvaluta == "USD" :
    doelvaluta = "EUR"
    resultaat = bedrag / WISSELKOERS_EUR_NAAR_USD

print(f"{bedrag} {bronvaluta} is gelijk aan {resultaat: .2f} {doelvaluta}")
