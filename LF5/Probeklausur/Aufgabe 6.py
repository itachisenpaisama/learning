# b)

print("Bitte geben Sie zwei ganze Zahlen ein:\n")

try:
    a = int(input("Erste Zahl:\n"))
    b = int(input("Zweite Zahl:\n"))
    if a > b:
        c = a - b
        print(f"{a} - {b} = {c}")
    elif b > a:
        c = b - a
        print(f"{b} - {a} = {c}")
    else:
       print(f"{b} - {a} = 0")
except ValueError:
    print("Bitte geben Sie eine gültige Zahl ein") 