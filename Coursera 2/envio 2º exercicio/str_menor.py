nomes = []
def menor_nome(list):
    """
    -> Função devolve o menor mome escrito
    param: lista de nomes
    """
    menor = cont = 0
    for i in list:
        nomes.append(i.strip())   
    for i in nomes:
        a = len(i)
        if cont == 0:
            menor = a
            nome_m = i.capitalize()
        if a < menor:
            menor = a
            nome_m = i.capitalize()
        cont +=1
    print(nome_m)
    return  nome_m

menor_nome(['Bárbara', 'JOSÉ  ', 'Bill'])
menor_nome(['maria', ' Paulo ', '  PAULO', 'Catarina  '])
menor_nome(['maria', 'josé', 'PAULO', 'Catarina'])

