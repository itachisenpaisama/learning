# Erstellen Sie ein Programm, das zwei Zahlen x und y einliest und alle Zahlen von
# x bis y (einschließlich) ausgibt. Verwenden Sie eine for-Schleife.

import sys # Importiert System-Funktionen für den sauberen Abbruch

while True: # Endlosschleife, die bei Fehlern neu startet
    try:
        Zahl_x = int(input("Erste Zahl:\n")) # Liest die Startzahl x ein
        Zahl_y = int(input("Zweite Zahl:\n")) # Liest die Endzahl y ein
        if Zahl_x < Zahl_y: # Prüft, ob x kleiner als y ist (damit die Schleife Sinn macht)
            for i in range(Zahl_x, Zahl_y + 1, 1): # Schleife von x bis y (y+1 ist exklusiv)
                print(i) # Gibt die aktuelle Zahl aus
            print("Programmende.") # Abschlussmeldung
            break # Beendet die while-Schleife nach Erfolg
        else: # Falls x größer oder gleich y ist
            print("Macht so keinen Sinn, merkste selber.") # Fehlermeldung
        
    except ValueError: # Fängt ungültige Eingaben ab
        print("Zahlen Bruder...Zahlen.")
    except KeyboardInterrupt: # Fängt manuellen Abbruch mit STRG+C ab
        print("Programmende.")
        sys.exit()
        