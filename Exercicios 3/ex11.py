
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("aprovado")
else:
    nota_exame = float(input("digite a nota do exame: "))
    media = (media + nota_exame) / 2
    if media >= 5:
        print("aprovado")
    else:
        print("reprovado")