lista = [-15, 13, 6, 17, -12, 0, 17]
lista_neg = []
lista_pos = []
lista_0 = []
# separação de listas, negativos, positivos
for elemento in lista:
    if elemento < 0:
        lista_neg.append(elemento)
    elif elemento > 0:
        lista_pos.append(elemento)
    else:
        lista_0.append(elemento)
print(lista_neg)
print(lista_pos)
print(lista_0)

# lista com valor dobrado, sendo adicionado em uma nova lista
lista_dobro = []

for elemento in lista:
    lista_dobro.append(2*elemento)
print(lista_dobro)

#soma de dois itens conforme posição, de cada lista diferente
listasom = []
for elemento1, elemento02 in zip(lista_pos, lista_neg):
    listasom.append(elemento1 + elemento02)
print(listasom)

# compreenção de listas em uma linha
lista_dob_pos = [2*elemento for elemento in lista if elemento > 0]

print(lista_dob_pos)

for indice in range(len(lista)):
    print(indice, lista[indice])

