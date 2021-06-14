'''
numero = int(input("Digite um numero = "))
tot = 0
for c in range(1,numero+1):
	if numero % c ==0:
		print('\033[33m',end='')
		tot = tot+1
	else:
		print('\033[31m',end='')
	print('{}'.format(c), end='')
print('\nsispromotion_log.txt\033[m0 numero {} foi divisivel {} vezes'.format(numero,tot))
if tot == 2:
        print('E por isso ele é PRIMO!')
else:
        print('E por isso ele não é PRIMO!')
'''
'''
import math
def eh_primo(n):
        raiz=int(math.sqrt(n))
        for d in range(2, raiz+1):
                if n % d==0:
                        return False
        return True
numero = int(input("Digite um número: "))
if eh_primo(numero):
        print("O número {} é primo".format(numero))
else:
        print("O número {} Não é primo".format(numero))
'''
n = int(input("Verificar numeros primos ate: "))
mult=0

for count in range(2,n):
    if (n % count == 0):
        print("Múltiplo de",count)
        mult += 1

if(mult==0):
    print("É primo")
else:
    print("Tem",mult," múltiplos não é primo",n)
