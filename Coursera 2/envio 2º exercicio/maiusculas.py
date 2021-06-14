frase =[]
maiuscula= ''
def maiusculas(frase):   
    maiuscula= ''
    for i in frase:  
        letra = i
        if letra.isalpha():
            letra_m = letra.upper()    
        if letra_m == letra.upper():
            if letra == letra_m:
                 maiuscula += letra
    print(maiuscula)
    return maiuscula

maiusculas('Programamos em python 2?')
# deve devolver 'P'

maiusculas('Programamos em Python 3.')
# deve devolver 'PP'

maiusculas('PrOgRaMaMoS em python!')
# deve devolver 'PORMMS'
