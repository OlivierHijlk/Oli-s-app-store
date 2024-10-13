from subprocess import call

# functie keuze menu
def keuzemenu():
    # While true lus, blijft herhalen
    while True:
        print("---Oli's app store---")
        # Titel keuze menu
        print("Keuze Menu: \n")
        # keuze 1
        print("1. Speel Raad het Getal")
        # keuze 2
        print("2. Speel Galgje")
        # keuze 3
        print("3. Afsluiten")

        # de input en keuze zijn het zelfde
        keuze = input("Maak een keuze: ")

        # als keuze 1 is wordt raad het getal gestart
        if keuze == '1':
            print("Raad het Getal spel wordt nu gestart!\n")
            call(["python", "Raad_het_getal.py"])
        # als keuze 2 is wordt galgje gestart
        elif keuze == '2':
            print("Galgje spel wordt nu gestart!\n")
            call(["python", "galgje.py"])
        # als keuze 3 is eindigt het programma
        elif keuze == '3': # programma eindigt
            print("De Programma wordt afgesloten :( ")
            break
        # alles anders dan keuze '1', '2', '3' speelt hij opnieuw af
        else:
            print("Ongeldige keuze, probeer opnieuw.")

# voert alleen uit als script direct wordt uitgevoerd
if __name__ == '__main__':
    # keuzemenu functie wordt aangeroepen
    keuzemenu()


""""
Stuk code waar ik trots op ben!

Bronnenlijst:
1. https://www.youtube.com/watch?v=cjXhbXWQxFE
2. https://www.youtube.com/watch?v=CUFIjz_U7Mo
3. https://www.youtube.com/watch?v=63nw00JqHo0
4. https://www.w3schools.com/python/default.asp
5. Leergroep: 'groep 6'
"""