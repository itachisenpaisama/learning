#Erweitern Sie das letzte Programm so, dass man eine untere und obere Grenze ein-
#geben kann und dann alle Zahlen und ihre Quadratzahlen in diesen Grenzen ausgibt.
untere_grenze = int(input("Geben Sie die untere Grenze ein: "))
obere_grenze = int(input("Geben Sie die obere Grenze ein: "))
for i in range(untere_grenze, obere_grenze + 1):
    quadrat = i * i
    print(f"Die Zahl: {i} hat die Quadratzahl: {quadrat}")