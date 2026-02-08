# Ein Kollege möchte ein Programm, das nach Eingabe der Datenmenge (in MB) und der
# Datenübertragungsrate (in Kbit/s) die Zeit berechnet, welche für die Übertragung der
# Datenmenge benötigt wird. Die Zeit soll in Minuten ausgegeben werden

import sys # Importiert das Modul sys, um das Programm bei Bedarf beenden zu können

print("Bitte geben Sie die Datenmenge in MB und die Datenübertragungsrate in Kbit/s an.") # Informiert den Benutzer über die erwarteten Eingaben

while True: # Startet eine Endlosschleife, damit das Programm bei fehlerhaften Eingaben nicht abstürzt, sondern neu startet
    try: # Versucht, den Eingabe- und Berechnungsblock auszuführen
        Datenmenge_MB = float(input("Datenmenge: \n")) # Fragt die Datenmenge ab und wandelt die Eingabe in eine Kommazahl um
        if Datenmenge_MB > 0: # Überprüft, ob die Datenmenge größer als 0 ist
            Datenübertragungsrate_Kbit = float(input("Datenübertragungsrate: \n")) # Fragt die Übertragungsrate ab und wandelt sie in eine Kommazahl um
            if Datenübertragungsrate_Kbit > 0: # Überprüft, ob die Rate größer als 0 ist (Teilen durch 0 oder negative Rate verhindern)
                Datenmenge_Kbit = Datenmenge_MB * 8 * 10 ** 3 # Wandelt MB in Kbit um (1 MB = 8 Mbit = 8000 Kbit)
                Übertragungsdauer_Sec = Datenmenge_Kbit / Datenübertragungsrate_Kbit # Berechnet die Dauer in Sekunden (Menge / Geschwindigkeit)
                Übertragungsdauer_Min = Übertragungsdauer_Sec / 60 # Wandelt die Sekunden in Minuten um
                print(f"Die Übertragung benötigt {Übertragungsdauer_Min:.2f} Minuten") # Gibt das Ergebnis auf 2 Nachkommastellen gerundet aus
                print("Programmende") # Signalisiert das Ende der Programmausführung
                break # Beendet die Schleife, da alles erfolgreich berechnet wurde
            else: # Falls die Rate <= 0 ist
                print("Wird wohl unendlich lange dauern.") # Gibt eine logische Fehlermeldung aus
        else: # Falls die Datenmenge <= 0 ist
            print("Braucht genau 0 Sekunden.") # Gibt eine logische Antwort für 0 Daten aus
    except ValueError: # Fängt den Fehler ab, wenn Text statt Zahlen eingegeben wurde
        print("Sollten schon Zahlen sein") # Weist den Benutzer freundlich auf den Fehler hin
    except KeyboardInterrupt: # Fängt den manuellen Abbruch mit STRG+C ab
      print("Programmende") # Bestätigt den Abbruch
      sys.exit() # Beendet das Programm sauber
                