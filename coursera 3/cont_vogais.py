
def  conta_letras(frase, contar="vogais"):
    vog_v = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    vog_c = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u',' ']
    cont_v = 0
    if contar == 'vogais':
        for c in frase:
            if c in vog_v:
                cont_v += 1
        print(cont_v)
        return cont_v
    else:
        for c in frase:
            if c not in vog_c:
                cont_v += 1
        print(cont_v)
        return cont_v
    
            
'''conta_letras('programamos em python')
# deve devolver 6
conta_letras('programamos em python', 'vogais')
# deve devolver 6
conta_letras('programamos em python', 'consoantes')
# deve devolver 13'''
