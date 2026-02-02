#Die Fakultät einer Zahl n wird so berechnet: n! = 1· 2· 3· · · · · n. Erstellen Sie ein
#Programm, das die Fakultät mit wiederholter Multiplikation berechnet
n = int(input("Geben Sie eine Zahl n ein: "))
fakultaet = 1
for i in range(1, n + 1):
    fakultaet = fakultaet * i
print(f"Die Fakultät von {n} ist: {fakultaet}")