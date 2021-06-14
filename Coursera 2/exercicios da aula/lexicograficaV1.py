palavras = []
m_lex = m_lexicografica = ''
nom_m = ''
def maior_lexi(list):
    cont = 0
    nom = ''
    for i in list:
        nom = i
        if cont == 0:
            maior = ord(i)
            nom_m = i
        else:
            if nom > nom_m:
                nom_m = i
        cont += 1 
    return nom_m

while True:
    resp = 'S'
    nomes = str(input('Digite uma palavra: ')).strip().upper()
    resp = str(input('Quer continuar [S/N]:')).upper()[0]
    palavras.append(nomes)
    if resp == 'N':
        break

p = maior_lexi(nomes)

print('-+-'*10)
print(f'O maior nome lexicográfico da lista é = {p}')
print('-+-'*10)        
