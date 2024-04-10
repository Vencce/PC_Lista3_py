a = float(input("digite o valor de a: "))
b = float(input("digite o valor de b: "))
c = float(input("digite o valor de c: "))

delta = (b**2) - (4*a*c)

if delta < 0:
    print("a equação não possui raízes reais")
elif delta == 0:
    print("a equação possui apenas uma raiz real")
else:
    print("a equação possui duas raizes reais")