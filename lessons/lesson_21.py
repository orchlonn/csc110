def RmvVwlsFrom(str): 
    str =  str.replace("a","").replace("e","").replace("i","").replace("o", "").replace("u", "")
    return str


print(RmvVwlsFrom('hello orchlon'))
