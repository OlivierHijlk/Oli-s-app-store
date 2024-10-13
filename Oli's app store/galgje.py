import random

# woorden uit woordenlijst
def woordlijst(bestand):
    # opent bestand en leest die
    f = open(bestand, 'r')
    # leest inhoud en split ze in lijst woorden
    woorden = f.read().splitlines()
    # closed file
    f.close()
    # kiest random woord uit woorden lijst
    return random.choice(woorden)

# Functie om de voortgang van het geraden woord te tonen
def vooruitgang(woord, correcteletters):
    # lege string om voortgang te laten zien
    voortgang = ''
    # loopt elke letter van geheime woord af
    for letter in woord:
        # als letter in correcteletters zit gaat die in de voortgang string
        if letter in correcteletters:
            voortgang += letter + ' '
        # anders wordt _ toegevoegd in string
        else:
            voortgang += '_ '
    # laat voortgang weer zien
    return voortgang

# Functie om het spel te starten
def start_spel():
    # Vraag de naam van de speler
    naam = input("Wat is je naam? ")
    print(f"Welkom, {naam}! Laten we beginnen met het spel.")

    # Kiest een random woord uit woorden.txt
    woord = woordlijst('woorden.txt')

    # hoeveel pogingen speler heeft
    max_pogingen = 11
    pogingenover = max_pogingen

    # lijst met correcte geraden letters
    correcteletters = []

    # spelt loopt als er nog pogingen overzijn
    while pogingenover > 0:
        print(f"Je hebt nog {pogingenover} pogingen.")
        print(f"Voortgang van het woord: {vooruitgang(woord, correcteletters)}")

        # Vraagt speler of ze letter of woord willen raden alles wordt in lowercase
        gok = input("Raad een letter of het hele woord: ").lower()

        # speler heeft woord proberen te raden
        if len(gok) == len(woord):
            if gok == woord:
                # speler heeft goed geraden
                print(f"Gefeliciteerd, {naam}! Je hebt het woord '{woord}' juist geraden!")
                break
            else:
                # fout geraden dus -1 poging
                print(f"Helaas, '{gok}' is niet het juiste woord.")
                pogingenover -= 1
        # speler heeft letter proberen te raden
        elif len(gok) == 1:
            if gok in woord:
                # speler heeft goed geraden
                print(f"Goed gedaan! De letter '{gok}' zit in het woord.")
                # als letter in gok zit wordt hij aan lijst correcte letters toegevoegd
                correcteletters.append(gok)
            else:
                # speler heeft niet goed geraden
                print(f"Helaas, de letter '{gok}' zit niet in het woord.")
                pogingenover -= 1
        else:
            print("Ongeldige invoer, probeer opnieuw.")

        # Of unieke letters in het te raden woord voorkomen in correcte letters lijst
        if set(woord) == set(correcteletters):
            # als de het aan elkaar gelijk is heb je gewonnen
            print(f"Gefeliciteerd, {naam}! Je hebt alle letters geraden, het woord was '{woord}'.")
            break
    # anders heb je helaas geen pogingen meer over en dus verloren
    else:
        print(f"Helaas, je hebt geen pogingen meer over. Het woord was '{woord}'.")

# roept start_spel aan waarmee het spel start
start_spel()

""""
Bronnen: 
1. https://www.w3schools.com/python/default.asp
2. https://www.youtube.com/watch?v=LpZmZs2_BC4&pp=ygUQcmVhZCBmaWxlIHB5dGhvbg%3D%3D
3. https://www.w3schools.com/python/python_sets.asp
4. https://www.youtube.com/watch?v=KWgYha0clzw&pp=ygUPcHl0aG9uIGZvciBsb29w
5. Leergroep: 'groep 6'
"""