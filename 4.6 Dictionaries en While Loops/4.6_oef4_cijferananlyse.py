cijfers = {
    "Nederlands": 7,
    "Engels": 6,
    "Wiskunde": 8,
    "Informatica": 9,
    "Geschiedenis": 5,
    "Aardrijkskunde": 7,
    "Biologie": 6
}

totale_som = 0
aantal_vakken = 0 
for vak, cijfer in cijfers.items():
    totale_som = totale_som + cijfer
    aantal_vakken = aantal_vakken + 1
gemiddelde = totale_som/ aantal_vakken
print("Het gemiddelde cijfer is:", round(gemiddelde, 1))

hoogste_cijfer = 0
hoogste_vak = ""
for vak, cijfer in cijfers.items():
    if hoogste_cijfer < cijfer:
        hoogste_cijfer = cijfer
        hoogste_vak = vak
print(f"Het vak met het hoogste cijfer is {hoogste_vak} met het cijfer {hoogste_cijfer}.")

laagste_cijfer = 10
laagste_vak = ""
for vak, cijfer in cijfers.items():
    if laagste_cijfer > cijfer: 
        laagste_cijfer = cijfer
        laagste_vak = vak
print(f"Het vak met het laagste cijfer is {laagste_vak} met het cijfer {laagste_cijfer}.")

print("Vakken met een voldoende:")
for vak, cijfer in cijfers.items():
    if cijfer >= 6:
        print(f"{vak}")

print("Vakken met een onvoldoende:")
for vak, cijfer in cijfers.items():
    if cijfer <= 6: 
        print(f"{vak}")
