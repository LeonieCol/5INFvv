persoon = {
    "naam":"Leonie",
    "leeftijd": 16,
    "school": "Van Veldeke",
    "hobby's": ["tennis", "Chiro"]
}

print("Naam:", persoon["naam"])
persoon["woonplaats"] = "Rummen"
persoon["leeftijd"] += 1
del persoon["school"]

print("Uiteindelijke Dictionary:")
print(persoon)
