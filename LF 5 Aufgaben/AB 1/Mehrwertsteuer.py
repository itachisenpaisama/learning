# Sie bekommen den Auftrag einen Mehrwertsteuer-Rechner zu erstellen. Das Programm
# muss in Python umgesetzt werden. Es muss den Einzelpreis, die Stückzahl und den Mehrwertsteuersatz einlesen. 
# Das Program soll den Nettowarenwert und Bruttopreis ausrechnen.

import sys  # Importiert das Modul sys, um das Programm bei Bedarf beenden zu können

print("Bitte geben Sie den Einzelpreis in €, die Stückzahl und ihren Mehrwertsteuersatz in % ein.") # Fordert den Benutzer zur Eingabe der Daten auf

while True: # Startet eine Endlosschleife, um Fehleingaben abfangen zu können
    try: # Versucht, den folgenden Code-Block auszuführen
        Einzelpreis = float(input("Einzelpreis:\n")) # Liest den Einzelpreis ein und wandelt ihn in eine Kommazahl um
        if Einzelpreis > 0: # Prüft, ob der Einzelpreis positiv ist
            Stückzahl = int(input("Stückzahl:\n")) # Liest die Stückzahl ein und wandelt sie in eine Ganzzahl um
            if Stückzahl > 0: # Prüft, ob die Stückzahl positiv ist
                Mehrwerststeuer_Prozent = float(input("Mehrwertsteuersatz:\n")) # Liest den Mehrwertsteuersatz ein
                if Mehrwerststeuer_Prozent >= 0: # Prüft, ob der Steuersatz nicht negativ ist
                    Warenwert_Netto = Einzelpreis * Stückzahl # Berechnet den Nettowarenwert
                    Mehrwertsteuer_Wert = Warenwert_Netto * Mehrwerststeuer_Prozent / 100 # Berechnet den absoluten Mehrwertsteuerbetrag
                    Warenwert_Brutto = Warenwert_Netto + Mehrwertsteuer_Wert # Berechnet den Bruttopreis
                    print(f"Der Nettopreis beträgt: {Warenwert_Netto:.2f} €\nDie Mehrwertsteuer beträgt: {Mehrwertsteuer_Wert:.2f} €\nDer Bruttopreis beträgt: {Warenwert_Brutto:.2f} €") # Gibt die berechneten Werte formatiert aus
                    print("Programmende") # Informiert über das Ende des Programms
                    break # Beendet die Schleife nach erfolgreicher Berechnung
                else: # Falls der Steuersatz negativ ist
                    print("Lern mal bitte was eine Mehrwertsteuer ist.") # Gibt eine Fehlermeldung aus
            else: # Falls die Stückzahl <= 0 ist
                print("Geh woanders hin wenn du nichts kaufen willst.") # Gibt eine Fehlermeldung aus
        else: # Falls der Einzelpreis <= 0 ist
            print("Umsonst gibts hier nichts.") # Gibt eine Fehlermeldung aus

    except ValueError: # Fängt Fehler ab, wenn Buchstaben statt Zahlen eingegeben wurden
        print("Probiers doch nochmal :)") # Fordert den Benutzer freundlich zur erneuten Eingabe auf
    except KeyboardInterrupt: # Fängt den manuellen Abbruch durch STRG+C ab
        print("Programm beendet") # Bestätigt den Abbruch
        sys.exit() # Beendet das Programm vollständig