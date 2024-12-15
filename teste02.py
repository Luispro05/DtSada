def calcula_desconto(valor):
	if valor >=500:
		desconto = valor*0,2
	elif valor <500 and valor >= 300: 
		desconto = valor*0.15
	elif valor<300 and valor >=100:
		desconto = valor*0,1
	else:
		desconto = 0
	return float(desconto)

valor = 450
calcula_desconto(valor)

print("Seu desconto é de R$", calcula_desconto(valor))