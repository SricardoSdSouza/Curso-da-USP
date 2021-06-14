'''def fazAlgo(string):
    pos = 0
    string1 = ''
    string = string.lower()
    stringMa = string.upper()
    while pos < len(string):
        if pos % 2 == 0:
            string1 = string1 + stringMa[pos]
        else:
            string1 = string1 + string[pos]
        pos = pos + 1
    return string1

print(fazAlgo('paralelepipedo'))'''

def fazAlgo(string):
    pos = 0
    string1 = ''
    while pos < len(string):
        if string[pos] != '':
            string1 = string1 + string[pos]
        pos = pos + 1
        string1 = string1.capitalize()
    return string1

print(fazAlgo('É UM TESTE'))
