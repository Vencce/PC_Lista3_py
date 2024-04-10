idade_homem1 = int(input("Digite a idade do primeiro homem: "))
idade_homem2 = int(input("Digite a idade do segundo homem: "))

idade_mulher1 = int(input("Digite a idade da primeira mulher: "))
idade_mulher2 = int(input("Digite a idade da segunda mulher: "))

if idade_homem1 > idade_homem2:
    homem_mais_velho = idade_homem1
    homem_mais_novo = idade_homem2
else:
    homem_mais_velho = idade_homem2
    homem_mais_novo = idade_homem1

if idade_mulher1 > idade_mulher2:
    mulher_mais_velha = idade_mulher1
    mulher_mais_nova = idade_mulher2
else:
    mulher_mais_velha = idade_mulher2
    mulher_mais_nova = idade_mulher1

soma_idades = homem_mais_velho + mulher_mais_nova

produto_idades = homem_mais_novo * mulher_mais_velha

print("A soma das idades do homem mais velho com a mulher mais nova é:", soma_idades)
print("O produto das idades do homem mais novo com a mulher mais velha é:", produto_idades)
