# c)

try:
    n = int(input("Bitte geben Sie eine Zahl ein:\n"))
    for i in range(2,n+1,2):
        print(i)
except ValueError:
    print("Bitte geben Sie eine gültige Zahl ein.")