import random
#Aantal pogingen
pogingen = 7
#geheim getal dat de computer kiest.
getal_comp = random.randrange(1,101)

# vraagt de naam
naam = str(input("Hoe heet je: "))
#De naam en hoeveel pogingen om het getal te raden
print(f"{naam} Je hebt {pogingen} pogingen om het getal tussen 1 en 100 te raden!")


# For-loop om de gebruiker te laten raden
for i in range(pogingen):
    # Vraag de gebruiker om een getal te raden
    getal = int(input(f"Poging {i+1}: Welk getal kies jij: "))

    # Controleer of de gebruiker het juiste getal heeft geraden
    if getal == getal_comp:
        print(f"Gefeliciteerd! Je hebt het juiste getal {getal_comp} geraden in {i+1} pogingen.")
        break  # Verlaat de loop omdat het getal is geraden
    elif getal < getal_comp:
        print("Te laag! Probeer het opnieuw.")
    else:
        print("Te hoog! Probeer het opnieuw.")

# Als de gebruiker alle pogingen heeft gebruikt zonder het juiste getal te raden
if getal != getal_comp:
    print(f"Helaas, je hebt al je pogingen gebruikt. Het juiste getal was {getal_comp}.")


""""
 1. Het getal (random)
 2. input van speler (getal)
 vergelijking tussen 1 en 2
controle conditie goed/fout
als fout nog een keer.
Dit hierboven hadden we in de klas besproken en had ik opgeschreven
"""

"""
Bronnenlijst:
1. https://www.youtube.com/watch?v=B2tviDGFq84
2. https://www.w3schools.com/python/default.asp
3. Leergroep: 'groep 6'
"""