soma = 0
for i in range(1, 4):
    nota = float(input(f" Informe a sua nota: {i}:"))

    soma = soma + nota

    media = soma / 3

if media >= 7:
    print("Aprovado!")
    print(f'Sua nota foi: {media}')
elif media >= 5:
    print("Recuperação!")
    print(f'Sua nota foi: {media}')
else:
    print('Reprovado!')
    print(f'Sua nota foi: {media}')