Liste = []

while True:
    Eingabe = input("Zahl eingeben")
    if Eingabe.lower() == "q":
        break
    try:
       Zahl = float(Eingabe)
       Liste.append(Zahl)
    except ValueError:
        print("Ungültige Eingabe. Bitte gib eine Zahl oder q an") 
    
    
print(Liste)
    
