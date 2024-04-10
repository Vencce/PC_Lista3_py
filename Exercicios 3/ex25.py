#Escrever um algoritmo para ler dois valores e uma das seguintes operações a serem
a = int(input("digite o primeiro valor: "))
b = int(input("digite o segundo valor: "))

op = int(input("digite a operação (1-Adição, 2-Subtração, 3-Multiplicação, 4-Divisão): "))

if op == 1:
    print("A adição é: ", a + b)
elif op == 2:
    print("A subtração é: ", a - b)
elif op == 3:
    print("A multiplicação é: ", a * b)
elif op == 4:
    print ("A divisão é: ", a / b)
else:
    print("operação inválida")