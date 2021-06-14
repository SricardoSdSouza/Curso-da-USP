
def busca(lista, x):
    primeiro = 0
    ultimo = len(lista)-1

    while primeiro <= ultimo:
        # operador // significa divisão inteira (truncada)
        meio = (primeiro + ultimo) // 2  

        if lista[meio] == x:
            print(meio)
            return meio
        
        elif x < lista[meio]:
            ultimo = meio - 1
            
        else:
            primeiro = meio + 1
        print(meio)         
    # retorna False se o elemento não foi encontrado
    return False 


#print(busca(['a', 'c', 'c', 'd'], 'c'))
#print('##'*5)
#print(busca([1, 2, 3, 4, 5], 6))
#print('##'*5)
#print(busca([1, 2, 3, 4, 5, 6], 4))
#print('##'*5)

