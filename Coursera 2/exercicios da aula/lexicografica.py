palavras = []

def maior_lexi(list):
    maior = cont = 0
    m_lex = ''
    while True:
        for i in list:
            n = i
            p = ord(i[0])
            if cont == 0:
                maior += p
                m_lex = n
            if p > maior:
                maior = p
                m_lex = n
            cont += 1
        return maior, m_lex

while True:
    resp = 'S'
    nomes = str(input('Digite uma palavra: ')).strip().upper()
    resp = str(input('Quer continuar [S/N]:')).upper()[0]
    palavras.append(nomes)
    if resp == 'N':
        break

p = maior_lexi(palavras)

print('-+-'*10)
print(f'O maior nome lexicográfico da lista é = {p[1]}')
print('-+-'*10)        
