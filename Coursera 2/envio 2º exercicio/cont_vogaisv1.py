
def  conta_letras(frase, contar="vogais"):
    vog = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    cont_v = 0
    if contar == 'vogais':
        for c in frase:
            if c in vog:
                cont_v += 1
        print(f'Existem {cont_v} vogais nesta frase!')
        print()
        print('='*35)
        return cont_v
    else:
        for c in frase:
            if c not in vog and c != ' ':
                cont_v += 1
        print(f'Existem {cont_v} consoantes nesta frase!.')
        print('='*35)
        return cont_v
    
            
conta_letras('programamos em python')
# deve devolver 6
conta_letras('programamos em python', 'vogais')
# deve devolver 6
conta_letras('programamos em python', 'consoantes')
# deve devolver 13
