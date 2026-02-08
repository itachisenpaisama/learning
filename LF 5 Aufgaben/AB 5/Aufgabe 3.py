# Erstellen Sie ein Python-Programm, das eine Liste mit den vorgegebenen Städtenamen enthält.
# a) Geben Sie alle Städtenamen aus, die den Buchstaben "a" enthalten
# b) Geben Sie alle Städtenamen aus, die kürzer als 5 Zeichen sind

# Liste der vorgegebenen Städte
Städte = ["Berlin", "Paris", "Rom", "Wien", "London", "Madrid", "Oslo", "Bern", "Prag", "Athen"]

# a) Ausgabe aller Städte, die ein 'a' (oder 'A') enthalten
print("Alle Städte, die den Buchstaben 'a' enthalten:")
letter = "a"

for stadt in Städte:
    # Wir wandeln den Städtenamen in Kleinbuchstaben um (.lower()), 
    # damit auch 'A' (wie in Athen) gefunden wird.
    if letter in stadt.lower():
        print(stadt)

print() # Leerzeile für bessere Lesbarkeit

# b) Ausgabe aller Städte mit weniger als 5 Zeichen
print("Alle Städte, die kürzer als 5 Zeichen sind:")

for stadt in Städte:
    # len() gibt die Anzahl der Zeichen zurück
    if len(stadt) < 5:
        print(stadt)
