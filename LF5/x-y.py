#Erstellen Sie ein Programm, das zwei Zahlen x und y einliest und alle Zahlen von
#x bis y (einschließlich) ausgibt
x = int(input("Geben Sie die Zahl x ein: "))
y = int(input("Geben Sie die Zahl y ein: "))
for i in range(x, y + 1):
    print(i)