numero = int(input("Digite um número de 4 dígitos (entre 1000 e 9999): "))

if 1000 <= numero <= 9999:
    dezena_unidade = numero % 100
    milhar_centena = numero // 100

    terceiro_numero = dezena_unidade + milhar_centena

    if terceiro_numero ** 2 == numero:
        print("O número", numero, "obedece à característica.")
    else:
        print("O número", numero, "não obedece à característica.")
else:
    print("Número inválido. Por favor, digite um número de 4 dígitos entre 1000 e 9999.")
