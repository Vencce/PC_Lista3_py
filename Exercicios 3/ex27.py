a = float(input("digite o valor de a: "))
b = float(input("digite o valor de b: "))
c = float(input("digite o valor de c: "))

if a < b + c and b < a + c and c < a + b:
    if a == b and b == c:
        print("triângulo equilátero")
    elif a == b or b == c or a == c:
        print("triângulo isósceles")
    else:
        print("triângulo escaleno")
else:
    print("os valores lidos não formam um triângulo")
