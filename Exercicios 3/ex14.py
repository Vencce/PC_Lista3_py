#Ler o nome de 2 times e o número de gols marcados na partida. Escrever o nome do vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE.

time1 = input("digite o nome do time 1: ")
time2 = input("digite o nome do time 2: ")

gols1 = int(input("digite o numero de gols do time 1: "))
gols2 = int(input("digite o numero de gols do time 2: "))

if gols1 > gols2:
    print(time1 + " venceu")
elif gols1 < gols2:
    print(time2 + " venceu")
else:
    print("Empate")