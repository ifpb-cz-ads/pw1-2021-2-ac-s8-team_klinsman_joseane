# 6) Reescreva o programa da abaixo de forma a utilizar for em vez de while.

def soma(L):
    total = 0
    for x in range(5):
        total += L[x]
    return total

