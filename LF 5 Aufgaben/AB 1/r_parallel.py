# Der Gesamtwiderstand zweier parallelgeschalteter Widerstände soll nach der Eingabe der beiden Widerstände berechnet werden

print("Bitte geben Sie den Wert der beiden Widerständer in Ohm ein.") # Gibt eine Anweisung an den Benutzer aus
import sys # Importiert das Modul sys, um das Programm beenden zu können
while True: # Startet eine Endlosschleife, die läuft, bis sie explizit beendet wird
    try: # Versucht, den folgenden Code-Block auszuführen und auf Fehler zu prüfen
        Widerstand_1 = float(input("Erster Widerstand: \n")) # Liest den ersten Widerstand als Kommazahl ein
        Widerstand_2 = float(input("Zweiter Widerstand: \n")) # Liest den zweiten Widerstand als Kommazahl ein

        Widerstand_Gesamt = (1 / Widerstand_1 + 1 / Widerstand_2) ** - 1 # Berechnet den Gesamtwiderstand (Kehrwert der Summe der Kehrwerte)
        print(f"Der Gesamtwiderstand beträgt {Widerstand_Gesamt:.2f} Ohm") # Gibt das Ergebnis auf 2 Nachkommastellen gerundet aus
        print("Programmende") # Gibt eine Abschlussmeldung aus
        break # Beendet die while-Schleife nach erfolgreicher Berechnung
    except ValueError: # Fängt Fehler ab, wenn keine gültige Zahl eingegeben wurde
        print("Musst schon Zahlen eingeben.") # Gibt eine Fehlermeldung bei falschem Datentyp aus
    except ZeroDivisionError: # Fängt den Fehler ab, wenn durch 0 geteilt wird (Widerstand = 0)
        print("Widerstand kann leider nicht Null sein.") # Gibt eine Fehlermeldung bei Division durch Null aus
    except KeyboardInterrupt: # Fängt den Abbruch durch STRG+C ab
        print("Programmende") # Gibt eine Abschlussmeldung aus
        sys.exit() # Beendet das Programm sofort und vollständig

        
