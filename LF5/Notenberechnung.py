#Erstellen Sie ein Python-Programm, das solange Noten von der Tastatur (jede einzeln
#mit input()) einliest und in einer Liste speichert, bis der Benutzer etwas anderes als eine
#Note von 1 bis 6 eingibt. Anschließend soll die Liste der eingegebenen Noten ausgegeben
#werden.

#b) Erweitern Sie das Programm so, dass zusätzlich die beste und die schlechteste Note
#bestimmt und ausgegeben werden.

#c) Erweitern Sie das Programm so, dass die Notenliste sortiert ausgegeben wird.

#d) Erweitern Sie das Programm so, dass die Durchschnittsnote berechnet und ausgegeben
#wird.

Noten_Liste = []
i = 0

print("Gib Noten zwischen 1 und 6 ein. Gib eine Zahl außerhalb dieser Reichweite ein, um die Eingabe zu beenden:")
while True:
    Note = int(input())
    if Note >= 1 and Note <= 6:
        Noten_Liste.append(Note)
    else:
        break

#Noten_Liste.pop()    
Noten_Liste.sort()
print(f"Die Noten lauten: {Noten_Liste}")


print(f"Die beste Note ist eine {Noten_Liste[0]} und die schlechteste ist eine {Noten_Liste[len(Noten_Liste)-1]}")

summe = 0

for i in range(0,len(Noten_Liste)):
    summe = sum(Noten_Liste[i])
    
average = summe / len(Noten_Liste)

print(f"Der Durchschnitt ist {average:.1f}")