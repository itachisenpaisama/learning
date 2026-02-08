# Erstellen Sie ein Programm, das einen Namen von der Tastatur einliest und dann
# viermal „Hallo “ und den Namen ausgibt
i = 0
name = input("Geben Sie Ihren Namen ein: ")
for i in range (0, 4):
    print("Hallo " + name)