#Entrar com o ano de nascimento de uma pessoa e imprimir a idade dela. Verificar se o ano digitado é válido.

ano_nasc = int(input("digite o ano de nascimento: "))   
ano_atual = int(input("digite o ano atual: "))

idade = ano_atual - ano_nasc

if ano_nasc > ano_atual:
    print("ano invalido")
else:
    print(idade)
