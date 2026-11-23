def farenheit_naar_celcius(temp_f):
    celsius = (temp_f - 32) * 5 / 9
    return round(celsius, 1)


def celcius_naar_farenheit(temp_c):
    fahrenheit = temp_c * 9 / 5 + 32
    return round(fahrenheit, 1)

print("Welke conversie wil je uitvoeren?")
print("1. Fahrenheit naar Celsius")
print("2. Celsius naar Fahrenheit")

keuze = input("Maak je keuze (1 of 2): ")
