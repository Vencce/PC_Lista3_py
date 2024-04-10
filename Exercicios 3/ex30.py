salario = float(input("Digite o salário do funcionário: "))

if salario < 10000:
    reajuste = salario * 0.55
elif salario <= 25000:
    reajuste = salario * 0.20
else:
    reajuste = salario * 0.10

novo_salario = salario + reajuste

print("Salário antes do reajuste: R$", salario)
print("Valor do reajuste: R$", reajuste)
print("Novo salário após o reajuste: R$", novo_salario)