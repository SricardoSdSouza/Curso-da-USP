n = int(input("Digite um número inteiro: "))
mult=0

for count in range(2,n):
    if (n % count == 0):
        mult += 1

if(mult==0):
    print("primo")
else:
    print("não primo")
