lista = [12, 15, 13 , 9]

print(lista)

lista.append(3)

print(lista)


lista.insert(0, 19)

print(lista)

print(len(lista))

lista2=[5,23,21]
lista.extend(lista2)
print(lista)

lista.pop(2)

print(lista)

lista.remove(5)

print(lista)

print("Quantidade de 2 na lista", lista.count(2))

print("posição do numero", lista.index(3)) 

lista.sort()

print(lista)

lista.sort(reverse=True)

print(lista)

print(sum(lista))

print(max(lista))

print(min(lista))

