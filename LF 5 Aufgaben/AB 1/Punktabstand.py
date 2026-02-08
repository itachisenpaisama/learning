# Der Abstand zweier Punkte P1 = (x1, y1) und P2 = (x2, y2) soll nach der Eingabe der x 
# und y Werte berechnet und ausgegeben werden

import math # Importiert das Modul math für mathematische Funktionen wie Wurzelziehen
import sys # Importiert das Modul sys, um das Programm beenden zu können

print("Geben Sie die Koordinaten der beiden Punkte ein, um deren Abstand zu berechnen") # Gibt eine Anweisung an den Benutzer aus

while True: # Startet eine Endlosschleife, die läuft, bis sie explizit beendet wird
    try: # Versucht, den folgenden Code-Block auszuführen und auf Fehler zu prüfen
        X_1 = float(input("Erster Punkt x: \n")) # Liest die x-Koordinate des ersten Punktes ein
        Y_1 = float(input("Erster Punkt y: \n")) # Liest die y-Koordinate des ersten Punktes ein
        X_2 = float(input("Zweiter Punkt x: \n")) # Liest die x-Koordinate des zweiten Punktes ein
        Y_2 = float(input("Zweiter Punkt y: \n")) # Liest die y-Koordinate des zweiten Punktes ein

        Abstand = math.sqrt((X_2 - X_1) ** 2 + (Y_2 - Y_1) **2) # Berechnet den euklidischen Abstand mit dem Satz des Pythagoras
        print(f"Der Abstand der Punkte beträgt: {Abstand:.1f}") # Gibt das Ergebnis auf 1 Nachkommastelle gerundet aus
        print("Programmende") # Gibt eine Abschlussmeldung aus
        break # Beendet die while-Schleife nach erfolgreicher Berechnung
    except ValueError: # Fängt Fehler ab, wenn keine gültige Zahl eingegeben wurde
        print("Das keine Zahl nh") # Signalisiert dem Nutzer auf entspannte Weise, dass die Eingabe falsch war
    except KeyboardInterrupt: # Fängt den Abbruch durch STRG+C ab
        print("Programmende") # Gibt eine Abschlussmeldung aus
        sys.exit() # Beendet das Programm sofort und vollständig
