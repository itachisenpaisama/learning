
temperaturen = [12.5, 18.0, 21.3, 16.8, 9.4, 23.1]

import math

summe = sum(temperaturen)
print(f"Die Summe aller Temperaturen beträgt:\n{summe:.1f}")
durchschnitt = summe / len(temperaturen)

print(f"Der Durchschnitt aller Temperaturen beträgt:\n{durchschnitt:.1f} ")