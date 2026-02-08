# Die Fakultät einer Zahl n wird so berechnet: n! = 1 · 2 · 3 · · · · · n. Erstellen Sie ein
# Programm, das die Fakultät mit wiederholter Multiplikation berechnet. Verwenden Sie eine for-Schleife.

import sys # Importiert System-Funktionen für den sauberen Abbruch

print("Fakultätrechner.") # Titel

while True: # Endlosschleife für Fehlerbehandlung
    try:
        n = int(input("Gib eine Zahl ein:\n")) # Liest die Zahl n ein
        if n >= 0: # Fakultät ist für negative Zahlen nicht definiert (im Schulkontext)
            Fakultät = 1 # Initialisiert das Ergebnis mit 1 (neutrales Element der Multiplikation)
            for i in range(1, n+1, 1): # Schleife von 1 bis n
                Fakultät *= i # Multipliziert den aktuellen Wert dazu (Fakultät = Fakultät * i)
            print(f"{n}! = {Fakultät}") # Gibt das Ergebnis aus
            print("Programmende.")
            break # Beendet das Programm
        else:
            print("Mit negativen Zahlen ist das nicht so einfach.") # Fehler bei negativen Zahlen
    except ValueError: # Fängt falsche Eingaben ab
        print("Versuchs doch nochmal.")
    except KeyboardInterrupt: # Fängt Abbruch ab
        print("Programmende:")
        sys.exit()