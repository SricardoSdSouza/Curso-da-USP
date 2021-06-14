def soma_lista(lista=list()):
    if len(lista) >= 1:
        #retira o ultimo elemento da lista e soma em outra lista
        return lista.pop() + soma_lista(lista)
    else:
        return 0

