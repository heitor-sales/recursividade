def printstr(string):
    if string == '':
        print(string)
        return
    
    print(string[0])
    newstring = string[1:]
    if len (newstring) > 0:
        return printstr(newstring)

printstr('uva')