#Escrever um algoritmo para ler a quantidade de horas aula dadas por dois professores 
# e o valor por hora recebido por cada um. Mostrar na tela qual dos professores tem o salário total maior.

horas_professor1 = float(input("digite a quantidade de horas do professor 1: "))
horas_professor2 = float(input("digite a quantidade de horas do professor 2: "))

valor_hora_professor1 = float(input("digite o valor por hora do professor 1: "))
valor_hora_professor2 = float(input("digite o valor por hora do professor 2: "))

salario_professor1 = horas_professor1 * valor_hora_professor1
salario_professor2 = horas_professor2 * valor_hora_professor2

if salario_professor1 > salario_professor2:
    print("professor 1 tem o maior salario, com o valor de: ", salario_professor1)
else:
    print("professor 2 tem o maior salario, com o valor de: ", salario_professor2)
