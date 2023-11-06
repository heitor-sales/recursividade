def printInverse (string):
    if len(string) <= 1:
        print(string)
        return
    
    print(string[-1])
    newstring = string[0:-1]
    if len (newstring) > 0:
        return printInverse(newstring)
    
printInverse('uva')