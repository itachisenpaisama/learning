# Erstellen Sie ein Programm, das einen Namen von der Tastatur einliest und dann
# viermal „Hallo “ und den Namen ausgibt. Verwenden Sie dabei eine for-Schleife

Name = str(input("Gib bitte deinen Namen ein:\n")) # Liest den Namen als String ein

for i in range(0,4): # Schleife läuft 4-mal (von 0 bis 3)
    print(f"Hallo {Name}.") # Gibt "Hallo" gefolgt vom eingegebenen Namen aus