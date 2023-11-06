def invertString(string):
    if len(string) <= 1:
        return string
    
    newstring = string[0:-1]
    return string[-1] + invertString(newstring)

print(invertString('uva'))