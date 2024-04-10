#Entrar com a sigla do estado de uma pessoa e imprimir uma das mensagens: “Carioca, Paulista, Mineiro ou Outros”

sigla = input("digite a sigla do estado: ")

if sigla == "RJ" or sigla == "rj" or sigla == "Rj":
    print("Carioca")
elif sigla == "SP" or sigla == "sp" or sigla == "Sp":
    print("Paulista")
elif sigla == "MG" or sigla == "mg" or sigla == "Mg":
    print("Mineiro")
else:
    print("Outros")