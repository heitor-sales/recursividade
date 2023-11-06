def recusiveLenght(string):
    if len(string) == 0:
        return 0
    
    newstring = string[1:]
    return 1 + recusiveLenght(newstring)

print(recusiveLenght('uva'))