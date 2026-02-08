# a)

name = input("Name:\n")

# b)

print(name)

# c)

try:
    i = int(input("Zahl:\n"))
except ValueError:
    print("Das keine Zahl bruv.")
    
# d)

x = "abc"

print(x * 3)