opcao = int(input("Digite a opção (1 para ordem crescente, 2 para ordem decrescente, 3 para o maior valor entre os outros 2): "))
a = float(input("Digite o primeiro valor (a): "))
b = float(input("Digite o segundo valor (b): "))
c = float(input("Digite o terceiro valor (c): "))

if opcao == 1:
    valores_ordem_crescente = sorted([a, b, c])
    print("Valores em ordem crescente:", valores_ordem_crescente)
elif opcao == 2:
    valores_ordem_decrescente = sorted([a, b, c], reverse=True)
    print("Valores em ordem decrescente:", valores_ordem_decrescente)
elif opcao == 3:
    valores = [a, b, c]
    maior = max(valores)
    valores.remove(maior)
    valores.insert(1, maior)
    print("Valores com o maior valor entre os outros dois:", valores)
else:
    print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
