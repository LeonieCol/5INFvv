limiet = int(input("Voer een limiet in: "))

priemgetallen = []
teller = 2

while teller <= limiet:
    deler = 2
    is_priem = True

    while deler < teller:
        if teller % deler == 0:
            is_priem = False
            break
        deler += 1

    if is_priem:
        priemgetallen.append(teller)
    teller += 1

print(priemgetallen)


