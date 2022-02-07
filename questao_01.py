#1) Escreva uma função que retorne o maior de dois números. Valores esperados:
# máximo(5,6) == 6
# máximo(2,1) == 2
# máximo(7,7) == 7 

def maiorValor(a, b) :
    if(a>b):
        return a
    else:
        return b

print("máximo(5,6) == %d" % maiorValor(5,6))
print("máximo(2,1) == %d" % maiorValor(2,1))
print("máximo(7,7) == %d" % maiorValor(7,7))