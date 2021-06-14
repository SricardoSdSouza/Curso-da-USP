nomes = []
def menor_nome(list):
    """
    -> Função devolve o menor mome escrito
    param: lista de nomes
    """
    menor = cont = 0
    for i in list:
        a = len(i)
        if cont == 0:
            menor = a
            nome_m = i.capitalize()
        if a < menor:
            menor = a
            nome_m = i.capitalize()
        cont +=1
    print(nome_m)
    return menor, nome_m


'''while True:
    resp = 'S'
    nom = str(input('Digite um nome: ')).strip().upper()
    resp = str(input('Quer continuar? [S/N]:')).upper()[0]
    nomes.append(nom.strip()) 
    if resp == 'N':
        break'''
    
#nomes =['ana','joao','aninha','Pedro','joni']
#men = menor_nome(['maria', 'josé', 'PAULO', 'Catarina'])
menor_nome(['maria', 'josé', 'PAULO', 'Catarina'])
#print(menor_nome(nome_m))
'''print('-+-'*10)
print(f'O menor nome da lista é = {men[1]}')
print('-+-'*10)
'''
