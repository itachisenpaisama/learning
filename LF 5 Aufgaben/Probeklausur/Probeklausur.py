# Es soll eine Zeichenkette von der Tastatur eingelesen werden. Dabei soll Name: angezeigt werden. 
# Das Ergebnis soll in der Variablen name gespeichert werden

# b) Der Wert der Variablen name soll ausgegeben werden.



# name = input("Gib namen an du hs:\n")

# print(name)

# c) Einlesen einer Integer-Zahl von der Tastatur und Speichern 
# der Zahl in der Variablen i.

# i = int(input("zahl"))

# d) Ausgeben der Zeichenkette 'abc' dreimal direkt (ohne Zeilenumbrüche
# und Leerzeichen) hintereinander.

# print("abc"* 3) 

# 5)
# Erstellen Sie ein Python-Programm, das den Benutzer auffordert, eine Zahl einzugeben.
# Das Programm soll ausgeben, ob die Zahl gerade oder ungerade ist.
# Falls der Benutzer keine Zahl eingibt, soll die Meldung Bitte geben Sie eine gültige
# Zahl ein ausgegeben werden.



# try:
   # Eingabe = int(input("Geben Sie eine Zahl ein:\n"))
    # if Eingabe % 2 == 0:
      #  print("gerade")
    # else:
      #  print("ungerade")
# except ValueError:
  #  print("Gib gültig")

# Erstellen Sie ein Python-Programm, das zwei ganze Zahlen a und b von der Tastatur einliest.

# try:
    # a = int(input("Erste Zahl:\n"))
   # b = int(input("Zweite Zahl:\n"))

    # if a > b:
        # print(a - b)
    # elif b < a:
        # print(b - a)
    # else:
        # print("0")
 # except ValueError:
    # print("du huen gib ne zahl ein")

# n = int(input("Zahl:\n"))
# for i in range(2,n + 1):
    # if i % 2 == 0:
        # print(i)

temperaturen = [12.5 , 18.0 , 21.3 , 16.8 , 9.4 , 23.1]

summe = sum(temperaturen)

print(f"Die Summe ist {summe:.1f}")

durchschnitt = summe / len(temperaturen)

print(f"Der Durchschnitt ist {durchschnitt:1f})



   
