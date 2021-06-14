def fazAlgo(string):
    pos = len(string)
    stringMi = string.lower()
    string = string.upper()
    stringRe = ''
    while pos >= 0:
        if string[pos-1] == 'A' or string[pos-1] == 'E' or string[pos-1] == 'I' or string[pos-1] == 'O' or string[pos-1] == 'U':
            stringRe = stringRe + string[pos-1]
        else:
            stringRe = stringRe + stringMi[pos-1]
        pos = pos -1
    return stringRe

#if__name__ == '__main__':
print(fazAlgo('teste'))
print(fazAlgo('o ovo do acestruz'))
print(fazAlgo('A CASA MUITO ENGRAÇADA'))
print(fazAlgo('A TELEvisão queBROU'))
print(fazAlgo('A Vaca Amarela'))
