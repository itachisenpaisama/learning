# Erstellen Sie ein Programm, das alle Zahlen von 1 bis 15 und ihre Quadratzahlen
# ausgibt. Verwenden Sie eine for-Schleife.

for i in range(1, 16, 1): # Schleife von 1 bis 15 (16 ist exklusiv)
    print(f"Zahl: {i}") # Gibt die aktuelle Zahl aus
    Quadrat = i ** 2 # Berechnet das Quadrat der aktuellen Zahl
    print(f"Quadratzahl: {Quadrat}") # Gibt das Quadrat aus