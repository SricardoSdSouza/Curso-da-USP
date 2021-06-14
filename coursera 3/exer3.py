def calculo(x, y = 10, z = 5):
    return x + y * z;

#print(calculo(1,2,3))#resposta 7


#print(calculo(7,2))#resposta 17
#print(calculo(,12,10)) erro de sintaxe
#print(calculo())#erro de sintaxe
#print(calculo(7))# resposta 57

'''def horario_em_segundos(h, m, s):
    assert h >= 0 and m >= 0 and s >= 0
    return h * 3600 + m * 60 + s'''

#print(horario_em_segundos (1,2,3))

def fazAlgo(string):
    pos = len(string)-1
    stringMi = string.lower()
    string = string.upper()
    stringRe = ""
    while pos >= 0:
        if string[pos] == 'A' or string[pos] == 'E' or string[pos] == 'I' or string[pos] == 'O' or string[pos] == 'U':
            stringRe = stringRe + string[pos]
        else:
            stringRe = stringRe + stringMi[pos]
        pos = pos - 1
    return stringRe

if __name__ == "__main__":
    print(fazAlgo("teste"))
    print(fazAlgo("o ovo do avestruz"))
    print(fazAlgo("A CASA MUITO ENGRAÇADA"))
    print(fazAlgo("A TELEvisão queBROU"))
    print(fazAlgo("A Vaca Amarela"))
