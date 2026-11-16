while True:
    getal_1 = float(input("Voer het eerste getal in: "))
    operator = input("Voer de operator in (+, -, *, /): ")
    getal_2 = float(input("Voer het tweede getal in: "))

    if operator == "+":
        resultaat = getal_1 + getal_2
    elif operator == "-":
        resultaat = getal_1 - getal_2
    elif operator == "*":
        resultaat = getal_1 * getal_2
    elif operator == "/":
        if getal_2 == 0:
            print("Delen door nul is niet mogelijk.")
            resultaat = None
        else:
            resultaat = getal_1 / getal_2
    else:
        print("Ongeldige operator.")
        resultaat = None

    if resultaat is not None:
        print(f"{getal_1} {operator} {getal_2} = {resultaat}")

    while True:
        antwoord = input("Wil je nog een berekening uitvoeren? (ja/nee): ").strip().lower()
        if antwoord == "ja":
            break
        elif antwoord == "nee":
            break
        else:
            print("Ongeldig antwoord. Voer 'ja' of 'nee' in.")

    if antwoord == "nee":
        break
