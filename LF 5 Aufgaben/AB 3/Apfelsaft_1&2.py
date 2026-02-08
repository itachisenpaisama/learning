# Eine Firma verkauft Apfelsaft. Der Preis richtet sich nach der Anzahl der gekauften Kisten.
# 1-10 Kisten kosten jeweils 8 Euro, 11-99 Kisten kosten jeweils 7 Euro, 100-1000 Kosten
# jeweils 6 Euro und ab 1001 Kisten kostet jede Kiste 5 Euro. Erstellen Sie ein Programm,
# das die Anzahl der Kisten einliest und den Gesamtpreis berechnet

# Nachdem Sie mit dem Preisrechner etwas herumgespielt haben fällt Ihnen auf, dass der
# Gesamtpreis manchmal niedriger wird, wenn man mehr Flaschen kauft. Erweitern Sie das
# Apfelsaft-Programm so, dass die Anzahl der Kisten einliest und den Gesamtpreis berechnet
# und eine größere Bestellmenge vorschlägt, wenn der Gesamtpreis dadurch sinkt.

import sys # Import für Systemfunktionen (z.B. exit)

print("Preisrechner.")
print("Bis zu 10 Kisten kosten je 8,00 €\nBis zu 99 Kisten kosten je 7,00 €\nBis zu 1000 Kosten je 6,00 €\nAb 1001 kostet jede Kiste 5,00 €\n")
print("Geben Sie die Anzahl an Kisten die Sie kaufen möchten\n") # Benutzerinformation

while True: # Endlosschleife für Neustart bei Fehlern
    try:
        Kisten_Anzahl = int(input("Anzahl Kisten:\n")) # Einlesen der Kistenanzahl
        if Kisten_Anzahl > 0: # Prüfen ob Anzahl positiv ist
            Spartipp = ""  # Variable für potenziellen Spartipp initialisieren
            
            if Kisten_Anzahl <= 10: # Fall für 1 bis 10 Kisten (8 €)
                Preis = Kisten_Anzahl * 8 # Berechnung des regulären Preises
                if Preis > 11 * 7: # Prüfen ob 11 Kisten billiger wären (11 * 7 = 77€)
                    Spartipp = "Es wird billiger wenn sie 11 Kisten kaufen." # Spartipp merken
            
            elif Kisten_Anzahl <= 99: # Fall für 11 bis 99 Kisten (7 €)
                Preis = Kisten_Anzahl * 7 # Berechnung
                if Preis > 100 * 6: # Prüfen ob 100 Kisten billiger wären (100 * 6 = 600€)
                   Spartipp = "Es wird billiger wenn sie 100 Kisten kaufen." # Spartipp merken
            
            elif Kisten_Anzahl <= 1000: # Fall für 100 bis 1000 Kisten (6 €)
                Preis = Kisten_Anzahl * 6 # Berechnung
                if Preis > 1001 * 5: # Prüfen ob 1001 Kisten billiger wären (1001 * 5 = 5005€)
                    Spartipp = "Es wird billiger wenn sie 1001 Kisten kaufen." # Spartipp merken
            
            else: # Fall ab 1001 Kisten (5 €)
                Preis = Kisten_Anzahl * 5 # Berechnung              
            
            # Ausgabe der Ergebnisse
            if Spartipp: # Wenn ein Spartipp existiert
                print(Spartipp) # Spartipp ausgeben
            print(f"Der Gesamtpreis beträgt: {Preis:.2f} €") # Gesamtpreis ausgeben
            print("Programmende") # Abschlussmeldung
            break # Programm erfolgreich beenden

        else: # Falls Anzahl <= 0
            print("Mach dich ab.") # Fehlermeldung bei ungültiger Anzahl
            
    except ValueError: # Abfangen von falschen Eingaben
        print("Das Crazy.")        
    except KeyboardInterrupt: # Abfangen von Abbruch
        print("Programmende")
        sys.exit()