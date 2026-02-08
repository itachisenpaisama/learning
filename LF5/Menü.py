#Erstellen Sie ein Programm für ein textgeführtes Menü. Das heißt, es soll eine Aus-
#wahl mit Menüfunktionen angezeigt werden (Programmende (Q), Werte einlesen (E),
#Werte ausgeben (A), Werte ändern (Ä) und Hilfe (H)).
#Diese Auswahl soll immer wieder angezeigt werden und der Benutzer nachfolgend nach
#seiner Auswahl gefragt werden. Ist die Auswahl Q wird das Programm beendet.
#Die anderen Funktionen sind wie folgt:
#E Einlesen eines Werts und Speichern in der Variable wert
#A Ausgeben des Werts aus der Variable wert
#Ä Ausgeben des alten Werts und Einlesen des neuen Werts
#H Ausgabe der Programmbeschreibung und einer Beschreibung der einzelnen Funktionen

def print_menu():
    print("Willkommen zum textgeführten Menüprogramm!")
    print("Bitte wählen Sie eine der folgenden Optionen:")
    print("E - Werte einlesen")
    print("A - Werte ausgeben")
    print("Ä - Werte ändern")
    print("H - Hilfe")
    print("Q - Programmende")
print_menu()

Eingabe = input("Bitte geben Sie Ihre Auswahl ein: ")
wert = None
while True:
    if Eingabe == "E":
        wert = input("Bitte geben Sie einen Wert ein: ")
        print("Wert wurde gespeichert.")
    elif Eingabe == "A":
        if wert is not None:
            print(f"Der gespeicherte Wert ist: {wert}")
        else:
            print("Es wurde noch kein Wert gespeichert.")
    elif Eingabe == "Ä":
        if wert is not None:
            print(f"Der alte Wert ist: {wert}")
        else:
            print("Es wurde noch kein Wert gespeichert.")
        wert = input("Bitte geben Sie den neuen Wert ein: ")
        print("Wert wurde geändert.")
    elif Eingabe == "H":
        print_menu()
    elif Eingabe == "Q":
        print("Programm wird beendet. Auf Wiedersehen!")
        break
    else:
        print("Ungültige Auswahl. Bitte versuchen Sie es erneut.")
    Eingabe = input("Bitte geben Sie Ihre Auswahl ein: ")
        