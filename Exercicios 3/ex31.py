temperatura = int(input("Digite a temperatura desejada para o alumínio (em °C): "))

if temperatura >= 1000:
    print("Temperatura inválida. Digite um valor inferior a 1000°C.")
elif temperatura <= 500:
    print("Temperatura Inválida")
elif temperatura < 700:
    print("Aquecimento Ligado em 100%")
elif temperatura < 735:
    print("Aquecimento Ligado em 50%")
elif temperatura >= 735 and temperatura <= 780:
    print("Aquecimento Desligado")
else:
    print("Superaquecimento")

