# Erstellen Sie ein Programm, das eine Zahl y einliest und alle Zahlen von 1 bis y
# ausgibt. Verwenden Sie eine for-Schleife.

import sys # Importiert System-Funktionen für den sauberen Abbruch

while True: # Endlosschleife, die bei Fehlern neu startet
    try:
        n = int(input("Geben Sie eine Zahl ein:\n")) # Liest die Obergrenze n ein
        for i in range(1, n+1, 1): # Schleife von 1 bis n (n+1 ist exklusiv) mit Schrittweite 1
            print(i) # Gibt die aktuelle Zahl aus
    except ValueError: # Fängt ungültige Eingaben ab
        print("Das keine Zahl.")
    except KeyboardInterrupt: # Fängt manuellen Abbruch mit STRG+C ab
        print("Programmende.")
        sys.exit()
    else: # Wenn kein Fehler aufgetreten ist
        print("Programmende.")
        break # Programm beenden
