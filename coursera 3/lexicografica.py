lista = []
def  primeiro_lex(lista):
    maior = cont = 0
    m_lex = ''
    while True:
        for i in lista:
            n = i.strip()
            p = ord(i[0])
            if cont == 0:
                maior += p
                m_lex = n
            if p < maior:
                maior = p
                m_lex = n
            cont += 1
        print(m_lex)
        return m_lex
       
primeiro_lex(['oĺá', 'A', 'a', 'casa'])
# deve devolver 'A'
primeiro_lex(['AAAAAA', 'b'])
# deve devolver 'AAAAAA'
primeiro_lex(['maria', 'josé', 'PAULO', 'Catarina'])
primeiro_lex(['zé', 'lu', 'fê'])

