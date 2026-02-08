# Ein Händler verlangt für eine Flasche Sekt EUR 5. Bei Abnahme von mehr als 40 Flaschen
# ermäßigt sich der Preis auf EUR 4,50. Entwickeln Sie ein Programm, das die Anzahl der
# Flaschen einliest und den Gesamtpreis ausgibt

import sys # Importiert System-Funktionen für den sauberen Abbruch

print("Preisrechner.")
print("Eine Flasche Sekt kostet 5,00 €. Ab 41 Flaschen kostet eine Flasche 4,50 €.")
print("Bitte geben Sie die Anzahl an Flaschen an, die Sie kaufen möchten.") # Gibt Informationen für den Benutzer aus

while True: # Endlosschleife, damit bei Fehlern neu gestartet werden kann
    try:
        Flaschen_Anzahl = int(input("Anzahl Flaschen: \n")) # Liest die Flaschenanzahl als ganze Zahl ein
        if Flaschen_Anzahl > 0: # Prüft, ob mehr als 0 Flaschen bestellt wurden
            if Flaschen_Anzahl <= 40: # Bei 40 oder weniger Flaschen
                Preis = Flaschen_Anzahl * 5 # Normalpreis: 5€ pro Flasche
            else: # Bei mehr als 40 Flaschen
                Preis = Flaschen_Anzahl * 4.5 # Rabattierter Preis: 4,50€ pro Flasche
            print(f"Der Gesamtpreis beträgt: {Preis:.2f} €") # Gibt den Gesamtpreis formatiert auf 2 Nachkommastellen aus
            print("Programmende") # Zeigt das Ende an
            break # Beendet die Schleife bei erfolgreicher Berechnung
        else:
            print("Mach dich ab, wenn du nichts kaufen willst.") # Fehlermeldung bei 0 oder weniger Flaschen
    except ValueError: # Fängt ungültige Eingaben (z.B. Buchstaben) ab
        print("Und sonst so ?") # Fehlermeldung bei falschem Datentyp
    except KeyboardInterrupt: # Fängt manuellen Abbruch mit STRG+C ab
        print("Programmende") 
        sys.exit() # Beendet das Programm