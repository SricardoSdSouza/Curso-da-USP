from math import factorial
n = int(input('Digite o número: '))
c = n
f = 1
print('Calculando {}! = '.format(n))
while c > 0:
    print('{}'.format(c))
    print('X' if c>1 else'=')
    f = f*c
    c -= 1
print('{}'.format(f))
