import random

quiz = {
    "Wat is de hoofdstad van Frankrijk?": {
        "opties": ["A. Londen", "B. Parijs", "C. Berlijn", "D. Rome"],
        "antwoord": "B"
    },
    "Welke planeet staat het dichtst bij de zon?": {
        "opties": ["A. Venus", "B. Mars", "C. Mercurius", "D. Aarde"],
        "antwoord": "C"
    },
    "Hoeveel poten heeft een spin?": {
        "opties": ["A. 6", "B. 8", "C. 10", "D. 12"],
        "antwoord": "B"
    }
}

opnieuw = "ja"

while opnieuw == "ja":
    vragen = list(quiz.keys())
    random.shuffle(vragen)
    score = 0

    while len(vragen) > 0:
        vraag = vragen.pop(0)
        print(vraag)

        for optie in quiz [vraag]["opties"]:
            print(optie)

        gok = input("Antwoord (A/B/C/D): ").upper()

        if gok == quiz[vraag]["antwoord"]:
            print("Goed!")
            score = score + 1
        else: 
            print("Fout! Het was:", quiz[vraag]["antwoord"])

    print("Jouw score is:", score)
    opnieuw = input("Nog een keer spelen? (ja/nee): ").lower()