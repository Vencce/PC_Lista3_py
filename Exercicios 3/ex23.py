#Ler 3 valores (considere que não serão informados valores iguais) e escrevê-los em ordem crescente.

a = int(input("digite o primeiro valor: "))
b = int(input("digite o segundo valor: "))
c = int(input("digite o terceiro valor: "))

if a > b and a > c:
    if b > c:
        print("em ordem crescente:", a, b, c)
    else:
        print("em ordem crescente:", a, c, b)
elif b > a and b > c:
    if a > c:
        print("em ordem crescente:", b, a, c)
    else:
        print("em ordem crescente:", b, c, a)
else:
    if a > b:
        print("em ordem crescente:", c, a, b)
    else:
        print("em ordem crescente:", c, b, a)