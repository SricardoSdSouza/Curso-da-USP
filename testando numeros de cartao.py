''' Testar numero de cartão de credito '''
meuCartao = int(input("Digite o número do seu cartão de crédito"))
cartaolido = 1
encontreiMeuCartaoNaLista = False

while cartaolido !=0 and not encontreiMeuCartaoNaLista:
	cartaolido = int(input("Digite o número do próximo cartão de crédito"))
	if cartaolido == meuCartao:
		encontreiMeuCartaoNaLista = True
if encontreiMeuCartaoNaLista:
	print("Eba!!! Meu cartão esta na LIsta")
else:
	print("Xi!!! Meu cartão não esta na LIsta")