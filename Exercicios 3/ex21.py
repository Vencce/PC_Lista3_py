#Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.

a = int(input("digite o primeiro valor: "))
b = int(input("digite o segundo valor: "))
c = int(input("digite o terceiro valor: "))

if a > b and a > c:
    print(a, "é o maior")
elif b > a and b > c:
    print(b, "é o maior")
else:
    print(c, "é o maior")