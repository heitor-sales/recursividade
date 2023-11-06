def soma (number):
    if number < 0:
        return
    
    elif number == 0:
        return 0
    
    newnumber = number - 1

    return number + soma(newnumber)

print(soma(3))