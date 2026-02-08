# In dieser Aufgabe soll schrittweise ein Programm zur Verarbeitung von Schulnoten entwickelt
# werden

# a) Erstellen Sie ein Python-Programm, das solange Noten von der Tastatur (jede einzeln
# mit input()) einliest und in einer Liste speichert, bis der Benutzer etwas anderes als eine
# Note von 1 bis 6 eingibt. Anschließend soll die Liste der eingegebenen Noten ausgegeben
# werden.

# b) Erweitern Sie das Programm so, dass zusätzlich die beste und die schlechteste Note
# bestimmt und ausgegeben werden.

# c) Erweitern Sie das Programm so, dass die Notenliste sortiert ausgegeben wird.

# d) Erweitern Sie das Programm so, dass die Durchschnittsnote berechnet und ausgegeben
# wird.

print("Bitte geben Sie die Noten zwischen 1 und 6 ein.\nGeben Sie eine Zahl außerhalb ein, um die Eingabe zu beenden.")
Noten_Liste = [] 

# Erste Eingabe vor der Schleife (um die Bedingung prüfen zu können)
try:
    Eingabe = int(input("Note:\n"))
except ValueError:
    # Falls keine Zahl eingegeben wurde, setzen wir Eingabe auf 0, damit die Schleife nicht startet
    Eingabe = 0

# Schleife läuft, solange die Note gültig ist (zwischen 1 und 6)
while 1 <= Eingabe <= 6:
    # Gültige Note zur Liste hinzufügen
    Noten_Liste.append(Eingabe)
    
    # Nächste Note abfragen
    try:
        Eingabe = int(input("Note: "))
    except ValueError:
        # Bei ungültiger Eingabe (z.B. Buchstaben) beenden wir die Schleife sauber
        Eingabe = 0

# Prüfung: Wurden überhaupt Noten eingegeben?
if len(Noten_Liste) > 0:  # "if Noten_Liste:" wäre auch möglich
    # a) Ausgabe der Liste
    print(f"\nEingegebene Noten: {Noten_Liste}")

    # c) Liste sortieren
    Noten_Liste.sort()
    print(f"Sortierte Noten: {Noten_Liste}")

    # b) Beste und schlechteste Note
    # Da die Liste sortiert ist: [0] = kleinste Zahl (beste Note), [-1] = größte Zahl (schlechteste Note)
    print(f"Die beste Note ist eine {Noten_Liste[0]} und die schlechteste ist eine {Noten_Liste[-1]}.")

    # d) Durchschnitt berechnen
    # sum() addiert alle Noten, len() gibt die Anzahl zurück
    Durchschnitt = sum(Noten_Liste) / len(Noten_Liste)
    print(f"Der Durchschnitt ist {Durchschnitt:.1f}.") # .1f rundet auf 1 Nachkommastelle

else:
    print("Es wurden keine gültigen Noten eingegeben.")
