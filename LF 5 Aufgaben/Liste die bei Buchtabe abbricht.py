Liste = []
try:
    Zahl = float(input("Gib Zahl ein:"))
except ValueError:
    Zahl = "Q"
    
while Zahl != "Q":
    Liste.append(Zahl)
    
    try:
        Zahl = float(input("Gib Zahl ein:"))
    except ValueError:
        Zahl = "Q"
    
    
print(Liste)
    
