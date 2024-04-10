salario = float(input("digite o valor do seu salario: "))

if salario <= 400:
    novo_salario = salario + (salario * 0.15)
    print("o novo salario com o aumento de 15% e: ", novo_salario)
elif 400 < salario <= 700:
    novo_salario = salario + (salario * 0.12)
    print("o novo salario com o aumento de 12% e: ", novo_salario)
elif 700 < salario <= 1000:
    novo_salario = salario + (salario * 0.10)
    print("o novo salario com o aumento de 10% e: ", novo_salario)
elif 1000 < salario <= 1500:
    novo_salario = salario + (salario * 0.07)
    print("o novo salario com o aumento de 7% e: ", novo_salario)
elif 1500 < salario <= 2000:
    novo_salario = salario + (salario * 0.04)
    print("o novo salario com o aumento de 4% e: ", novo_salario)
elif salario > 2000:
    print("não houve aumento de salário")