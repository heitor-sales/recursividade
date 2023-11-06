def ispalindrome(string):
    if len(string) <= 1:
        return True
    
    newstring = string[1:-1]

    if len(newstring) == 1 and string[0] == string[-1]:
        return True

    if len(newstring) > 1:
        return ispalindrome(newstring)
    
    return False

print(ispalindrome('arara'))