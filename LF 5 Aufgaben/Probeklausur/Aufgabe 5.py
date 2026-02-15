# Gerade Ungerade Zahl

try:
    zahl = int(input("Bitte geben Sie eine Zahl ein:\n"))
    if zahl % 2 == 0:
        print("Die Zahl ist gerade.")
    else:
        print("Die Zahl ist ungerade.")
except ValueError:
    print("Bitte geben Sie eine gültige Zahl ein.")