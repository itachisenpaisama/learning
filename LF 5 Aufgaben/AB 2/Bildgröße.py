# Ihr Kollege ist begeistert von Ihrem letzten Programm und möchte jetzt noch ein Programm
# zur Berechnung der Größe von Bildern auf der Festplatte. Es soll aus der Breite, Höhe in
# Pixeln und der Farbtiefe in Bit den benötigten Platz auf der Festplatte in MiB berechnen.

import sys # Importiert System-Funktionen für sauberen Abbruch

print("Bildgrößen-Rechner.")
print("Bitte geben Sie Breite und Höhe in Pixel an sowie die Farbtiefe in Bits pro Pixel.")

while True: # Endlosschleife für Programm-Wiederholung
    try:
        Pixel_Breite = int(input("Breite: \n")) # Liest Breite als Ganzzahl ein
        if Pixel_Breite > 0: # Prüft auf gültige Breite
            Pixel_Höhe = int(input("Höhe: \n")) # Liest Höhe als Ganzzahl ein
            if Pixel_Höhe > 0: # Prüft auf gültige Höhe
                Pixel_Farbtiefe = int(input("Farbtiefe: \n")) # Liest Farbtiefe als Ganzzahl ein
                if Pixel_Farbtiefe > 0: # Prüft auf gültige Farbtiefe
                    Pixel_Anzahl = Pixel_Breite * Pixel_Höhe # Berechnet Gesamtanzahl der Pixel
                    Speicher_Bits = Pixel_Anzahl * Pixel_Farbtiefe # Berechnet Gesamt-Bits
                    Speicher_MiB = Speicher_Bits / 8 / 2**20 # Rechnet Bits in MiB um (Bits -> Bytes -> MiB)
                    print(f"Der belegte Speicherplatz beträgt: {Speicher_MiB:.2f} MiB") # Gibt Ergebnis in MiB aus
                    print("Programmende") # Abschlussmeldung
                    break # Beendet Schleife bei Erfolg
                else: 
                    print("Dumm!") # Fehlermeldung bei ungültiger Farbtiefe
            else:
                print("Das Bild will ich sehen.") # Fehlermeldung bei ungültiger Höhe
        else:
            print("Ja macht Sinn.") # Fehlermeldung bei ungültiger Breite
    except ValueError: # Fängt falsche Datentypen (z.B. Buchstaben) ab
        print("Das Crazy.")
    except KeyboardInterrupt: # Beendet bei STRG+C
        print("Programmende")
        sys.exit()