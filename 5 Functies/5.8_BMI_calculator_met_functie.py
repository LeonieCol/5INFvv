def bereken_bmi(gewicht, lengte):
    
    bmi = gewicht / (lengte*lengte)
    bmi = float(bmi)

    return bmi

gewicht = input("Wat is je gewicht: ")
gewicht = float(gewicht)

lengte = input("Wat is je lengte: ")
lengte = float(lengte)

print(bereken_bmi(gewicht,lengte))

