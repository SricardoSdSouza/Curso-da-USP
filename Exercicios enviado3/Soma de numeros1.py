n=int(input("Digite o nomero a ser somado = "))
soma = 0
while n!=0:
    resto = n%10
    n=(n-resto)/10
    soma =int(soma + resto)
print(soma)


