#Faça um algoritmo que leia um número inteiro e mostre uma mensagem indicando se este número é par ou ímpar.

valor = int(input("digite um valor: "))

if valor % 2 == 0:
    print("eh par")
else:
    print("eh impar")