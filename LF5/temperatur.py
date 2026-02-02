i = 0
summe = 0

for i in range(0, 5):
    temperatur = int(input("Geben Sie die Temperatur in Grad Celsius ein: "))
    summe = summe + temperatur
durchschnitt = summe / 6
print(f"Der Durchschnitt der bisher eingegebenen Temperaturen beträgt: {durchschnitt}")