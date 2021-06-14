''' Verificar se existem numeros iguais adjacentes '''
n = int(input("Digite um numero: "))
numeroDigitado = n
iguais = False
d_Ant = n % 10
n = n // 10
digito = 0

while n > 0 and not iguais:
        d_atual = n % 10
        n = n // 10
        if d_atual == d_Ant:
                iguais= True
        d_Ant = d_atual
if iguais:
        print("Contem números adjacentes iguais na sequência digitada",numeroDigitado)
else:
	print("Não contem números adjacentes iguais", numeroDigitado)
