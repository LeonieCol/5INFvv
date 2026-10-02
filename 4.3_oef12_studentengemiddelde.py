aantal_studenten = int(input("Hoeveel studenten zijn er? "))
naam = []
cijfer = []
som = 0

for i in range(1, aantal_studenten + 1):
    student_naam = input(f"Naam student {i}: ")
    naam.append(student_naam)
    student_cijfer = float(input(f"Cijfer van {student_naam}: "))
    cijfer.append(student_cijfer)

for i in range(0, aantal_studenten):
    resultaat = cijfer[i]
    som = som + resultaat
gemiddelde = som/aantal_studenten
    
print(f"Het gemiddelde is {gemiddelde}.")
