limiet = int(input("Voer een limiet in: "))

fib_reeks = []
a = 0
b = 1

while a <= limiet:
    fib_reeks.append(a)
    a, b = b, a + b

print(fib_reeks)