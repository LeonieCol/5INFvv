# AI-Logboek – Examen Python (Opdracht 4: Beleggingsportefeuille)
**Naam:** Leonie Colemont  
**Datum:** 27 november 2026  

---

### Prompt 1 (27 november 2026)
**Mijn prompt:**  
*"Examen Python – Opdracht 4: Beleggingsportefeuille [volledige examenopdracht geplakt]. Ik ben er zwaar door geïntimideerd."*

**Antwoord van de AI:**  
De AI stelde me gerust dat alle gevraagde onderdelen binnen hoofdstuk 1 tot en met 5 vallen en stelde een stappenplan voor: eerst de basisonderdelen werkend maken met lussen, daarna opdelen in functies (met parameters, `return` en docstrings), dan één van de twee uitbreidingen kiezen en tijdens het coderen meteen het logboek en de GitHub-commits bijhouden.

---

### Prompt 2 (27 november 2026)
**Mijn prompt:**  
*"1. Ik wou hiermee beginnen maar ik heb niet eens tegoei door wat ze van me willen: Per aandeel de gemiddelde, hoogste en laagste koers tonen."*

**Antwoord van de AI:**  
De AI legde uit hoe de startgegevens zijn opgebouwd (een dictionary met daarin per bedrijf `"aantal"` en een lijst `"koersen"`). Omdat de opdracht verbiedt om `sum()`, `min()` en `max()` te gebruiken voor deze berekening, legde de AI uit hoe we handmatig met een `for`-lus de som optellen en met `if`-statements de hoogste en laagste koers bijhouden.

---

### Prompt 3 (27 november 2026)
**Mijn prompt:**  
*"Oke dus stap een is eerst per aandeel een lijst maken die bijvoorbeeld koersentech heet en daar dat dan inzetten of is dit al fout?"*

**Antwoord van de AI:**  
De AI gaf aan dat aparte variabelen aanmaken wel werkt, maar leidt tot kopiëren en plakken van code (wat niet mag). In plaats daarvan gebruiken we een `for naam in aandelen:`-lus om met één tijdelijke variabele (`koersen = aandelen[naam]["koersen"]`) automatisch elk aandeel één voor één uit te lezen.

---

### Prompt 4 (27 november 2026)
**Mijn prompt:**  
*"Ik snap nog hoe we aan de slag moetn gaan met de variablen, maar ik weet niet hoe ik de laagste en hoogste koers moet vinden."*

**Antwoord van de AI:**  
De AI legde stap voor stap uit wat er in het geheugen van de computer gebeurt per ronde van de `for`-lus: we starten bij `totaal = 0`, `hoogste = koersen[0]` en `laagste = koersen[0]`, en bij elk volgend getal in de lijst tellen we op bij `totaal` en vergelijken we met `if koers > hoogste:` en `if koers < laagste:`. Na de lus delen we `totaal` door `len(koersen)`.

---

### Prompt 5 (27 november 2026)
**Mijn prompt:**  
*"Bruh wtf ik snap er niks meer van we moesten toch gwn het gemiddelde, hoogste en laagste berekenen. Ik zal al eens sturen wat ik heb gemaakt: [mijn eigen code met startgegevens en eerste for-lus]."*

**Antwoord van de AI:**  
De AI legde uit waarom we `min()`, `max()` en `sum()` niet mochten gebruiken (verplichte bouwsteen *Zelf rekenen*) en plakte de handmatige lus-berekening direct onder mijn eigen werkende lus, met juiste inspringing en een `f-string` met `:.2f` voor 2 decimalen.

---

### Prompt 6 (27 november 2026)
**Mijn prompt:**  
*"Oke is het eerste deel van mijn examenopdracht dan al klaar?"*

**Antwoord van de AI:**  
Ja, Basis-punt 1 werkt hiermee inhoudelijk volledig (en vinkt meteen *Zelf rekenen* en *f-strings* af). Wel gaf de AI de tip om dit werkende stuk code later nog netjes in een eigen functie met `return` en een docstring te gieten.

---

### Prompt 7 (27 november 2026)
**Mijn prompt:**  
*"Ik ga de code die ik nu heb nog eens doorsturen, kijk of de commentaren ook goed zijn of dat die beter moeten om alles echt duidelijk te maken voor mezelf: [code voor Basis 1 gestuurd]."*

**Antwoord van de AI:**  
De AI controleerde mijn code en commentaren. Mijn eigen voorbeelden bij "Ronde 1" waren goed, maar ik kreeg drie verbeterpunten:
1. De tijdelijke test-regel `print(naam, koersen)` verwijderen zodat er geen dubbele uitvoer is.
2. Erbij noteren waarom `laagste` op `koersen[0]` start en niet op `0` (anders blijft `0` altijd het kleinst).
3. Kleine opmaak- en spelfouten in de commentaren verbeteren en tussentijds committen op GitHub.

---

### Prompt 8 (27 november 2026)
**Mijn prompt:**  
*"Ja laten we daaraan beginnen [starten met Basis 2: rendement in % berekenen] en geef me de formule om het rendement te berekenen."*

**Antwoord van de AI:**  
De AI gaf de economische formule voor procentueel rendement `((laatste_dag - eerste_dag) / eerste_dag) * 100` en legde uit hoe je de eerste (`koersen[0]`) en laatste koers (`koersen[-1]`) uit de lijst haalt.

---

### Prompt 9 (27 november 2026)
**Mijn prompt:**  
*"Verbeter indien nodig, zet ook juiste commentaar erbij: [mijn opzetje voor rendement met twee for-lussen] en help me ook al opweg met de best en de slechtse aandoelen want het kan toch niet dat ik die zelf in de koersen moet gaan zoeken om dan zo te programmeren."*

**Antwoord van de AI:**  
De AI verbeterde mijn code door de overbodige tweede `for koers in koersen:`-lus weg te halen (omdat je alleen het eerste en laatste getal nodig hebt, niet alle dagen ertussen). Daarna legde de AI uit hoe we het beste en slechtste aandeel bijhouden met extreme startwaarden (`-999999` en `999999`).

---

### Prompt 10 (27 november 2026)
**Mijn prompt:**  
*"[Code voor beste en slechtste aandeel met een aparte for-lus en inspringende prints] meer commentaar voor de duidelijkheid toevoegen aub."*

**Antwoord van de AI:**  
De AI voegde het zoeken naar het beste en slechtste aandeel samen in één enkele `for naam in aandelen:`-lus (zodat de variabele `rendement` per aandeel wordt vergeleken) en zette de laatste twee `print`-regels helemaal links buiten de lus, zodat pas na afloop het eindresultaat getoond wordt in plaats van na elke stap. Daarnaast werd extra commentaar toegevoegd.

### Prompt 11 (27 november 2026)
**Mijn prompt:**  
*"Oke geef me dit vanaf nu onder iedere prompt en antwoord dat je geeft, nu volgende opdracht 3. Ik snap niet eens goed wat dit wil zeggen in mensentaal, laat staan in python. Kan je dat eens eerst even uitleggen zodat ik al weet wat de bedoeling is en wat mijn leerkracht verwacht van vraag 3?"*

**Antwoord van de AI:**  
De AI vertaalde opdracht 3 eerst naar gewone mensentaal met een rekenvoorbeeld op basis van de startgegevens:
1. Eerst bereken je de totale waarde van je portefeuille door voor elk aandeel `aantal * laatste koers` op te tellen bij het `cash`-bedrag (€ 557 + € 420 + € 519 + € 500 = € 1996,00).
2. Pas daarna kun je voor elk aandeel het procentuele aandeel in die totale waarde berekenen via `(waarde_aandeel / totale_waarde) * 100`. Omdat je het totaal eerst moet kennen voordat je kunt delen, heb je hiervoor in Python twee opeenvolgende `for`-lussen nodig.

### Prompt 12 (27 november 2026)
**Mijn prompt:**  
*"Ik ben natuurlijk begonnen met deel 1 van de oefening en ben al hierop gekomen: [mijn opzetje met `for aantal in stuks:` en `totaal_aandelen = stuks * koersen[-1]`]. Dit werkt duidelijk niet, ik heb een probleem met 'stuks' maar kom niet op de oplossing. Je mag de hele code veranderen als dat nodig is om het efficiënter te maken."*

**Antwoord van de AI:**  
De AI legde uit waarom `for aantal in stuks:` niet werkt: `stuks` is één los geheel getal (geen lijst), dus daar kun je geen `for`-lus op uitvoeren. Daarnaast wees de AI erop dat je de waarde van elk aandeel moet **optellen** bij het totaal (`totale_waarde = totale_waarde + waarde_aandeel`, startend vanaf `cash`), anders wordt de variabele elke ronde overschreven. Tot slot gaf de AI de code voor zowel Deel 1 (totale waarde) als Deel 2 (het percentage per aandeel in een tweede opeenvolgende `for`-lus).

**Wat ik zelf heb aangepast / fouten die ik heb opgelost:**  
* Ik had per ongeluk een `for`-lus gezet op een los getal (`stuks`) in plaats van op een lijst, en ik had `koersen` niet opgehaald uit de dictionary (`aandelen[naam]["koersen"][-1]`). Door die tweede lus weg te laten en de waarden netjes op te tellen bij `totale_waarde = cash`, werkte de berekening wel.

### Prompt 13 (27 november 2026)
**Mijn prompt:**  
*"Je mag me de oefening niet direct geven, ik ben nog steeds bezig aan een examenopdracht en we mogen gelukkig werken met AI maar het is niet de bedoeling dat ik de hele code ga kopiëren en plakken, ik wil dat je me gewoon mee op weg helpt en het me altijd eerst kort in mensentaal uitlegt zodat ik zelf ook al eens kan nadenken over een code."*

**Antwoord van de AI:**  
De AI paste zijn aanpak aan: geen kant-en-klare code meer, maar eerst een uitleg in mensentaal en daarna alleen hints zodat ik zelf kan programmeren. Voor Basis 4 (aandelen kopen en verkopen) legde de AI de logica achter het loket uit: vragen om het aandeel, de actie (kopen/verkopen) en het aantal stuks, en vervolgens controleren of er genoeg `cash` is bij aankoop (prijs + transactiekost) of genoeg aandelen bij verkoop (opbrengst - transactiekost).

### Prompt 14 (27 november 2026)
**Mijn prompt:**  
*"Oké, misschien kunnen we eens een functie gebruiken bij deze opdracht omdat dat nodig is, daarmee moet je me wel aan de gang helpen."*

**Antwoord van de AI:**  
De AI legde uit hoe een functie werkt aan de hand van een fabrieksmachine: parameters zijn de invoer (`aandelen`, `cash`, `transactiekost`), binnenin gebeurt de berekening en met `return cash` geeft de functie het aangepaste geldbedrag netjes terug (zoals vereist door de examenregels rond globale variabelen). De AI gaf enkel het lege geraamte van de functie `handel_aandelen` met een docstring, plus hints om `.lower()` te gebruiken en de returnwaarde op te vangen via `cash = handel_aandelen(...)`.