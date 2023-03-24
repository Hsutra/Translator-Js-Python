def is_float(text):
    try:
        float(text)
        return True
    except ValueError:
        return False

def ComandList(text):
    Operations = ['+', '-', '*', '/', '%', '**', '<', '>', '==', '!=', '<=', '>=', '=', '++', '--']
    Words = ['let', 'var', 'alert', 'if', 'else if', 'else', 'while', 'do', 'for']
    Separators = ['\n', ';', '{', '}', '[', ']', '(', ')']
    Dict = {}
    a = 1
    b = 1
    c = 1
    d = 1
    e = 1
    for i in Operations:
        Dict[i] = "O" + str(a)
        a += 1
    for i in Words:
        Dict[i] = "W" + str(b)
        b += 1
    for i in Separators:
        Dict[i] = "R" + str(c)
        c += 1

    for i in text:
        if((i.isdigit() or is_float(i)) and not(i in Dict)):
            Dict[i] = "D" + str(d)
            d += 1

    for i in text:
        if not(i in Dict):
            Dict[i] = "I" + str(e)
            e += 1
    Endlist = []

    for i in text:
        if(i in Dict):
            Endlist.append(Dict[i])
    return Endlist

f = open('file', 'r')
txt = ""
for i in f:
    txt += i
text = txt.split()
print(ComandList(text))

