#Calcule a soma de dois numeros, se o resultado digitado for maior que 10, mostre-o na tela

valorA = float(input("digite um valor : "))
valorB = float(input("digite outro valor : "))

soma = valorA + valorB

if soma > 10:
    print("soma maior que 10")
elif soma < 10:
    print("soma menor que 10")
else:
    print("soma igual a 10")

