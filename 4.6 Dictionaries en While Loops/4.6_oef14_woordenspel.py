import random

woorden = ["appel", "peer", "kiwi"]
geheim_woord = random.choice(woorden)
levens = 6
geraden_letters = set()

while levens > 0:
    zichtbaar_woord = ""
    for letter in geheim_woord:
        if letter in geraden_letters:
            zichtbaar_woord += letter
        else:
            zichtbaar_woord += "_"

    print(f"Woord: {zichtbaar_woord}")
    print(f"Levens: {levens}")

    if "_" not in zichtbaar_woord:
        print(f"Gewonnen! Het geheime woord was {geheim_woord}.")
        break
        
    gok = input("Raad een letter: ").lower().strip()

    if gok in geheim_woord:
        print("Goed geraden!")
        geraden_letters.add(gok)
    else: 
        print(f"Helaas de letter {gok} komt niet voor in het woord.")
        levens = levens - 1

if levens == 0:
    print(f"Helaas, je levens zijn op. Het gemeime woord was {geheim_woord}.")