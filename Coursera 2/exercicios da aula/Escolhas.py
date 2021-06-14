import time
n1=int(input('Primeiro valor: '))
n2=int(input('Segundo valor: '))
opção=0
opção1=0
while opção !=5:
    print('=-'*15)
    print(''' ==== MENU PRINCIPAL ==== 
[ 1 ] PARA SOMAR
[ 2 ] PARA MULTIPLICAR
[ 3 ] PARA COMPARAÇÃO
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA''')
    print('=-'*15)
    opção=int(input('QUAL É A SUA OPÇÃO::  '))
    if opção==1:
        s=n1+n2
        print('O resultada da soma é {}'.format(s))
    elif opção==2:
        s=n1*n2
        print('O resultado da multiplicação é {}'.format(s))
    elif opção==3:
        while opção1!=4:
            print('''OPÇÃO COMPARAÇÃO
        [ 1 ] PARA DETERMINAR O MAIOR VALOR
        [ 2 ] PARA DETERMINAR O MENOR VALOR
        [ 3 ] IGUAL
        [ 4 ] PARA SAIR DA OPÇÃO''')
            opção1=int(input(' SUA OPÇÃO: '))
            if opção1==1:
                if n1>n2:
                    print('{} é maior valor'.format(n1))
            elif n2>n1:
                print('{} é o maior valor'.format(n2))
            if opção1==2:
                if n1<n2:
                    print('{} é o menor valor'.format(n1))
            elif n2<n1:
                print('{} é o menor valor'.format(n2))
            if opção1==3:
                if n1==n2:
                    print('OS DOIS VALORES INSIRIDOS SÃO IGUAIS.')
            else:
                print('Valores diferentes!')
    if opção1==4:
        print('Saindo da opção 3.....')
        time.sleep(2)
        quit(opção1==3)
    elif opção==4:
        print('Informe os novos números')
        n1=int(input('Primeiro valor: '))
        n2=int(input('Segundo valor: '))
if opção==5:
    print('finalisando...')
    time.sleep(2)
    print('Fim do programa!.Obrigado pela experiencia.')
    quit()
