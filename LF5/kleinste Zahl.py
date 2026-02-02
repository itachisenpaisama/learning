# Erstellen Sie ein Programm, das die kleinste Zahl in einer Liste beliebiger Länge findet.


n = int(input("Wie viele Zahlen willst du eingeben?:"))
Zahlen_Liste = []

for i in range(0,n):
    Zahlen = float(input("Gib Zahlen ein amk:"))
    Zahlen_Liste.append(Zahlen)
    
Zahlen_Liste.sort()
print(f"Die kleinste Zahl die du eingegeben hast ist {Zahlen_Liste[0]}")
