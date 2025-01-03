# Abriu e leu o arquivo podendo substituir informacoes "r+"
with open("notas.txt", "r+", encoding= "utf-8") as f:
    f.write("6, 5, 4")
# Apenas leu o arquivo "r"
with open("notas.txt", "r", encoding= "utf-8") as f:
   conteudo = f.read()

   print(conteudo)
# separou as informaçoes e criou uma lista
   listan = conteudo.split(",")

   print(listan)

   print(listan[0])
# Transformou as informaçoes da lista em float para o calculo. e adc em uma lista diferente 
notacvs = []
for elemento in listan:
    notacvs.append(float(elemento))

print(notacvs)

media = sum(notacvs)/len(notacvs)

print(f"a média das notas é {media}")
# inseriu a informaçao com o valor da media, na segunda linha do arquivo 
with open("notas.txt", "a", encoding= "utf-8") as f:
    f.write("\n a Media é: 5.0")


    #OBS: SEMPRE O ARQUIVO VAI ESTAR EM STR, PARA CALCULAR E ANALISAR NUMEROS TEMOS QUE FAZER A CONVERSAO PARA INT, FLOAT ou BOOL