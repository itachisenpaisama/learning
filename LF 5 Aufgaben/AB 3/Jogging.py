#Beim Joggen soll der Puls nicht mehr als 140 Schläge pro Minute betragen. Entwickeln Sie
#ein Programm, dass den Puls erfragt und danach einen guten Ratschlag gibt.

import sys # Importiert System-Funktionen für den sauberen Abbruch

print("Geben Sie Ihren Puls für einen guten Ratschlag ein.") # Gibt eine Anweisung an den Benutzer aus

while True: # Endlosschleife, damit bei Fehlern neu gestartet werden kann
    try:
        Puls = int(input("Puls: \n")) # Liest den Puls als ganze Zahl ein
        if Puls <= 0: # Wenn der Puls 0 oder weniger ist
            print("Du bist tot.") # Ausgabe für unmöglichen Puls
        elif Puls > 0 and Puls <= 50: # Wenn der Puls sehr niedrig ist (1-50)
            print("Du solltest ins Krankenhaus.") # Medizinischer Ratschlag
        elif Puls > 50 and Puls < 140: # Wenn der Puls im normalen/sportlichen Bereich ist (51-139)
            print("Renn du Affe.") # "Motivierender" Ratschlag
        else: # Wenn der Puls 140 oder höher ist
            print("Mach Pause bitte.") # Warnung vor Überanstrengung
    except ValueError: # Fängt ungültige Eingaben (z.B. Buchstaben) ab
        print("Das kein Puls nh.") # Fehlermeldung bei falschem Datentyp
    except KeyboardInterrupt: # Fängt manuellen Abbruch mit STRG+C ab
        print("Programmende")
        sys.exit() # Beendet das Programm
    else: # Wird ausgeführt, wenn kein Fehler aufgetreten ist (try erfolgreich war)
        print("Programmende") # Abschlussmeldung
        break # Beendet die Schleife und damit das Programm
    