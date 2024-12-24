 # captando quantidade de notas 
n_notas = int(input("Digite o número de notas: "))

cont = 1

# Lista com as notas, inicio vazia
notas = []

while cont <= n_notas:

    nota_atual = float(input("Digite a nota: "))

    cont += 1

    notas.append(nota_atual)

media = sum(notas)/len(notas)

print(f"A média é:{media}")

