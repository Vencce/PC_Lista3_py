
nota1 = float(input("Digite a primeira nota parcial: "))
nota2 = float(input("Digite a segunda nota parcial: "))

media = (nota1 + nota2) / 2

if media >= 9.0:
    conceito = 'A'
elif media >= 7.5:
    conceito = 'B'
elif media >= 6.0:
    conceito = 'C'
elif media >= 4.0:
    conceito = 'D'
else:
    conceito = 'E'

print("Notas: {:.1f} e {:.1f}".format(nota1, nota2))
print("Média: {:.1f}".format(media))
print("Conceito:", conceito)

if conceito in ['A', 'B', 'C']:
    print("APROVADO")
else:
    print("REPROVADO")