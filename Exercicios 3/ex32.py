operacao = int(input("Digite um valor de 1 a 4 para selecionar a operação desejada (ou 0 para soma e 4 para média): "))

if operacao in [0, 1, 2, 3, 4]:
    numero1 = float(input("Digite o primeiro valor: "))
    numero2 = float(input("Digite o segundo valor: "))
    
    if operacao == 0:
        resultado = numero1 + numero2
        print("Resultado da soma:", resultado)
    elif operacao == 1:
        resultado = numero1 - numero2
        print("Resultado da subtração:", resultado)
    elif operacao == 2:
        resultado = numero1 * numero2
        print("Resultado da multiplicação:", resultado)
    elif operacao == 3:
        if numero2 != 0:
            resultado = numero1 / numero2
            print("Resultado da divisão:", resultado)
        else:
            print("Impossível dividir por zero.")
    else:
        media = (numero1 + numero2) / 2
        print("Média dos números:", media)
else:
    print("Valor errado. Programa encerrado sem cálculos.")
