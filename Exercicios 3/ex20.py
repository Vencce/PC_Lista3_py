#Ler 2 valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

a = int(input("digite o primeiro valor: "))
b = int(input("digite o segundo valor: "))

if a > b:
    print("em ordem crescente:", b, a)
else:
    print("em ordem crescente:", a, b)