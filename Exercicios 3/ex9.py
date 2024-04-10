#Entrar com a idade de uma pessoa e exibir a mensagem; Maior de idade, menor de idade ou acima de 65 anos.

idade = int(input("digite a idade: "))

if idade >= 65:
    print("acima de 65")
elif idade >= 18:
    print("maior de idade")
else:
    print("menor de idade")