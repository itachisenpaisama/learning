# Schreiben Sie ein Python-Programm, das nach Eingabe der gefahrenen Kilometer und der 
# Menge des verbrauchten Kraftstoffs den Durchschnittsverbrauch auf 100 Kilometer berechnet

import sys  # Importiert das Modul sys, um das Programm bei Bedarf beenden zu können

print("Bitte geben Sie die gefahrene Strecke in Kilometer an, sowie den verbrauchten Kraftstoff in Litern.") # Gibt eine Einleitung für den Benutzer aus

while True: # Startet eine Endlosschleife, damit das Programm bei Fehlern nicht sofort endet
    try: # Beginnt einen Block, in dem Fehler abgefangen werden können
        Strecke = float(input("Gefahrene Strecke:\n")) # Fragt die Strecke ab und wandelt die Eingabe in eine Kommazahl um
        if Strecke > 0: # Überprüft, ob die gefahrene Strecke größer als 0 ist
            Kraftstoff = float(input("Verbrauchter Kraftstoff:\n")) # Fragt den verbrauchten Kraftstoff ab und wandelt ihn in eine Kommazahl um
            if Kraftstoff > 0: # Überprüft, ob der Kraftstoffverbrauch größer als 0 ist
                Durchschnittsverbrauch = Kraftstoff / Strecke * 100 # Berechnet den Durchschnittsverbrauch auf 100 km
                print(f"Der Durchschnittsverbraucht ist {Durchschnittsverbrauch:.1f} L / 100 km") # Gibt das Ergebnis formatiert auf eine Nachkommastelle aus
                print("Programmende") # Gibt "Programmende" aus
                break # Beendet die Schleife, da die Berechnung erfolgreich war
            else: # Falls der Kraftstoff <= 0 ist
                print("Kannst ja schlecht nichts verbraucht haben.") # Gibt eine Fehlermeldung aus
        else: # Falls die Strecke <= 0 ist
            print("Mit 0 Kilometern verbraucht man nichts.") # Gibt eine Fehlermeldung aus
        
            
    except ValueError: # Fängt den Fehler ab, wenn keine gültige Zahl eingegeben wurde
        print("Bitte geben Sie eine Zahl ein.") # Informiert den Benutzer über die fahlgeschlagene Eingabe
    except KeyboardInterrupt: # Fängt den Fehler ab, wenn der Benutzer das Programm mit STRG+C abbricht
        print("Programm beendet.") # Bestätigt das Beenden des Programms
        sys.exit() # Beendet das Programm vollständig