# 2) Escreva uma função que receba dois números e retorne True se o primeiro número for múltiplo do segundo.

def Multiplo(x, y):
    if x % y == 0:
        return True
    else:
        return False
    
print(Multiplo(8, 4))
print(Multiplo(7, 3))
print(Multiplo(5, 5))
