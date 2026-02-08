# Erweitern Sie das letzte Programm so, dass man eine untere und obere Grenze ein-
# geben kann und dann alle Zahlen und ihre Quadratzahlen in diesen Grenzen ausgibt.
# Verwenden Sie eine for-Schleife

import sys # Importiert System-Funktionen für den sauberen Abbruch

print("Geben Sie einen Startwert und einen Endwert ein.") # Benutzeranweisung

while True: # Endlosschleife, die bei Fehlern neu startet
    try:
        a = int(input("Startwert:\n")) # Liest Startwert a ein
        b = int(input("Endwert: \n")) # Liest Endwert b ein
        if a < b: # Prüft, ob a kleiner als b ist (logische Grenzen)
            for i in range(a, b + 1, 1): # Schleife von a bis b (b+1 ist exklusiv)
                print(f"Zahl: {i}") # Gibt die aktuelle Zahl aus
                Quadrat = i ** 2 # Berechnet das Quadrat
                print(f"Quadratzahl: {Quadrat}") # Gibt das Quadrat aus
            print("Programmende.") # Abschlussmeldung
            break # Beendet die while-Schleife erfolgreich
        else: # Falls a >= b ist
            print("Kannst nicht zählen huh.") # Fehlermeldung
    except ValueError: # Fängt ungültige Eingaben ab
        print("Das üben wir noch.")
    except KeyboardInterrupt: # Fängt manuellen Abbruch mit STRG+C ab
        print("Programmende.")
        sys.exit()