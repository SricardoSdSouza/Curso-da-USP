def ordenada(lista):
    fim = len(lista)
    for i in range(fim -1):
        primeiro = i
        for n in range(i+1, fim):
            if lista[n] < lista[primeiro]:
                return False
    return True
                
        
            
#lista =[1,2,3,5,4]
#print(ordenada(lista))
