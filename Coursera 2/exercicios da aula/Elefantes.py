'''def incomodam(n):
    if n <= 0:
        return ''
    else:
        return 'incomodam ' + incomodam(n - 1)

def elefantes(n):
    if n <= 1:
        return ''
    else:
        count = 1
        string = 'Um elefante incomoda muita gente\n ' 
        while count < n:
            count += 1
            if count < n:
                string += str(count) + ' elefantes ' + incomodam(count) + 'muito mais '
                string += str(count) + ' elefantes ' + incomodam(count) + 'muita gente '
            else:
                string += str(count) + ' elefantes ' + incomodam(count) + 'muito mais\n '

    return string'''

def elefantes(n):
    if n <= 0: return ""
    if n == 1: return "Um elefante incomoda muita gente\n"
    return elefantes(n - 1) + str(n) + " elefantes " + incomodam(n) + ("muita gente" if n % 2 > 0 else "muito mais") + "\r\n"

def incomodam(n):
    if n <= 0: return ""
    if n == 1: return "incomodam "
    return "incomodam " + incomodam(n - 1)

print(elefantes(15))
    
