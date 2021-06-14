def incomodam(n):
    if n <= 0:
        return ""
    elif n % 1 == 0:
        return "incomodam " + incomodam(n-1)
    else:
        return ""

def elefantes(n):
    if n == 1:
        return "Um elefante incomoda muita gente"
    elif n == 2:
        return elefantes(n-1) + f"\n{n} elefantes "+ incomodam(n) +"muito mais" 
    elif n > 2:
        frase1 = f"\n{n-1} elefantes incomodam muita gente"
        frase2 = f"\n{n} elefantes "+ incomodam(n) +"muito mais"
        return elefantes(n-1) + frase1 +frase2
    else:
        return ""

print(elefantes(5))

import pytest
@pytest.mark.parametrize("test_input,expected", [
    (0, ""),
    (1, "Um elefante incomoda muita gente"),
    (2, "Um elefante incomoda muita gente\n2 elefantes incomodam incomodam muito mais"),
    (3,"Um elefante incomoda muita gente\n2 elefantes incomodam incomodam muito mais\n2 elefantes incomodam muita gente\n3 elefantes incomodam incomodam incomodam muito mais"),
    (4,"Um elefante incomoda muita gente\n2 elefantes incomodam incomodam muito mais\n2 elefantes incomodam muita gente\n3 elefantes incomodam incomodam incomodam muito mais\n3 elefantes incomodam muita gente\n4 elefantes incomodam incomodam incomodam incomodam muito mais"),
    (-1,""),
])
def test_eval(test_input, expected):
    assert elefantes(test_input) == expected
