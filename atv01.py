numero_sorteado = 15

numero_escolhido = int(input("Digite um numero ente 1 e 20: "))

while numero_escolhido != numero_sorteado:
    print(" voce errou, tente novamente..")

    numero_escolhido = int(input("Digite um numero ente 1 e 20: "))

print('parabens! Voce acertou!')