# Erstellen Sie ein Programm für ein textgeführtes Menü. Das heißt, es soll eine Auswahl 
# mit Menüfunktionen angezeigt werden (Programmende (Q), Werte einlesen (E),
# Werte ausgeben (A), Werte ändern (Ä) und Hilfe (H)).
# Diese Auswahl soll immer wieder angezeigt werden und der Benutzer nachfolgend nach
# seiner Auswahl gefragt werden. Ist die Auswahl Q wird das Programm beendet.
# Die anderen Funktionen sind wie folgt:
# E Einlesen eines Werts und Speichern in der Variable wert
# A Ausgeben des Werts aus der Variable wert
# Ä Ausgeben des alten Werts und Einlesen des neuen Werts
# H Ausgabe der Programmbeschreibung und einer Beschreibung der einzelnen Funktionen

import sys # Importiert System-Funktionen für den sauberen Abbruch

print("Willkommen im Menü.\n") # Begrüßung

def Auswahl(): # Funktion, um das Menü anzuzeigen
    print("Q: Programmende\nE: Wert einlesen\nA: Wert ausgeben\nÄ: Wert ändern\nH: Hilfe\n")

Auswahl() # Menü beim Start einmal anzeigen

def Hilfe(): # Funktion für die Hilfe-Ausgabe
    print("E: Einlesen eines Werts und Speichern.\nA: Ausgeben des Werts\nÄ: Ausgeben des alten Werts und Einlesen des neuen Werts\nH: Ausgabe der Programmbeschreibung und einer Beschreibung der einzelnen Funktionen")

Eingabe = "" # Initialisiert die Eingabe-Variable
Wert = "Du hast doch noch gar nichts eingegeben?" # Initialisiert die Wert-Variable mit einem Standardtext

while Eingabe != "Q" and Eingabe != "q": # Schleife läuft, solange nicht 'Q' oder 'q' eingegeben wird
    try:
        Eingabe = str(input("Geben Sie Ihre Auswahl ein:\n")) # Liest die Auswahl ein       
        if Eingabe != "Q" and Eingabe != "q": # Wenn nicht beendet werden soll
            if Eingabe == "E" or Eingabe == "e": # Wenn 'E' gedrückt wurde
                Wert = input("Geben Sie ihren Wert ein:\n") # Liest neuen Wert ein
                Auswahl() # Zeigt Menü an
            elif Eingabe == "A" or Eingabe == "a": # Wenn 'A' gedrückt wurde
                print(f"Der gespeicherte Wert ist: {Wert}") # Gibt aktuellen Wert aus
                Auswahl() # Zeigt Menü an
            elif Eingabe == "Ä" or Eingabe == "ä": # Wenn 'Ä' gedrückt wurde
                print(f"Der gespeicherte Wert ist: {Wert}") # Zeigt alten Wert
                Wert = input("Geben Sie ihren Wert ein:\n") # Liest neuen Wert ein
                Auswahl() # Zeigt Menü an
            elif Eingabe == "H" or Eingabe == "h": # Wenn 'H' gedrückt wurde
                Hilfe() # Zeigt Hilfe an
            else: # Bei ungültiger Eingabe
                print("Lesen kannste nicht? Merkste selber.") # Fehlermeldung       
    except KeyboardInterrupt: # Fängt manuellen Abbruch mit STRG+C ab
        print("Programmende.")
        sys.exit()
print("Programmende.")