numero1 = int(input("Digite o primeiro valor inteiro: "))
numero2 = int(input("Digite o segundo valor inteiro: "))

resto_divisao = numero1 % numero2

if resto_divisao == 1:
    soma_resto = numero1 + numero2 + resto_divisao
    print("A soma dos números mais o resto da divisão é:", soma_resto)

elif resto_divisao == 2:
    if numero1 % 2 == 0:
        print(numero1, "é par.")
    else:
        print(numero1, "é ímpar.")
    
    if numero2 % 2 == 0:
        print(numero2, "é par.")
    else:
        print(numero2, "é ímpar.")

elif resto_divisao == 3:
    resultado = (numero1 + numero2) * numero1
    print("O resultado da multiplicação é:", resultado)

elif resto_divisao == 4:
    if numero2 != 0:
        resultado = (numero1 + numero2) / numero2
        print("O resultado da divisão é:", resultado)
    else:
        print("Impossível dividir por zero.")

else:
    print("O quadrado do primeiro número é:", numero1 ** 2)
    print("O quadrado do segundo número é:", numero2 ** 2)
