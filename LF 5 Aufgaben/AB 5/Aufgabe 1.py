# a) Erstellen Sie ein Programm, das die kleinste Zahl in einer Liste beliebiger Länge findet.

import random  # Importiert das Modul für Zufallszahlen

liste = []  # Erstellt eine leere Liste
n = random.randint(5, 50)  # Bestimmt eine zufällige Länge der Liste zwischen 5 bis 50

# Schleife, die n-mal durchlaufen wird
for i in range(n):
    # Fügt der Liste eine zufällige Zahl zwischen 0 und 100 hinzu
    liste.append(random.randint(0, 100))

liste.sort()  # Sortiert die Liste aufsteigend (kleinste Zahl zuerst)
print(liste)  # Gibt die sortierte Liste aus

# Index 0 ist das erste Element (das kleinste bei aufsteigender Sortierung)
print(f"Die kleinste Zahl in der Liste ist {liste[0]}.")

# b) Erstellen Sie ein Programm, das die größte Zahl in einer Liste beliebiger Länge findet.

# Index -1 ist das letzte Element (das größte bei aufsteigender Sortierung)
print(f"Die größte Zahl in der Liste ist {liste[-1]}.")
