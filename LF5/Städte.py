#Erstellen Sie ein Python-Programm, das eine Liste mit den vorgegebenen Städtenamen enthält.
#(Berlin, Paris, Rom, Wien, London, Madrid, Oslo, Bern, Prag, Athen).
#a) Geben Sie alle Städtenamen aus, die den Buchstaben a enthalten.
#b) Geben Sie alle Städtenamen aus, die kürzer als 5 Zeichen sind.

Stadt_Liste = ["Berlin", "Paris", "Rom", "Wien", "London", "Madrid", "Oslo", "Bern", "Prag", "Athen"]

print("Alle Städte die ein a im Wort haben:")
letter = "a"
for i in Stadt_Liste:
    if letter in i.lower():
        print(f"{i}")
    
print("Alle Städte mit weniger als Buchstaben:")
for i in range(0,len(Stadt_Liste)):
    if len(Stadt_Liste[i]) <5:
        print(f"{Stadt_Liste[i]}")