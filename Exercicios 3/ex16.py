#Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o valor 
# da compra for menor que R$ 20,00; Caso contrário, o lucro será de 30%. Entrar com o 
# valor do produto e imprimir o valor da venda.

valor = float(input("digite o valor do produto: "))

if valor < 20:
    print("valor da venda: ", valor * 1.45)
else:
    print("valor da venda: ", valor * 1.30)