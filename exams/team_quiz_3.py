

def messString(String):
    letters = 'pPiImM'
    newStr = ''
    for i in String: 
        if i in letters: 
            newStr += i + '1'
        else:
            newStr += i
    return newStr


def messString(String):
    letters = 'pPiImM'
    for i in letters:
        if i in String:
            String = String.replace(i, i + '1')
            
    return String
            
res  = messString('pray')

print(res)