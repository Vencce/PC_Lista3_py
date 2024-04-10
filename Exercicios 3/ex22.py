#Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.

a = int(input("digite o primeiro valor: "))
b = int(input("digite o segundo valor: "))
c = int(input("digite o terceiro valor: "))

if a > b and a > c:
    if b > c:
        print(a + b)
    else:
        print(a + c)
elif b > a and b > c:
    if a > c:
        print(b + a)
    else:
        print(b + c)
else:
    if a > b:
        print(c + a)
    else:
        print(c + b)