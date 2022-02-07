#3) Escreva uma função que receba o lado (l) de um quadrado e retorne sua área (A = lado^2).
# Valores esperados:
# área_quadrado(4) == 16
# área_quadrado(9) == 81

def areaQuadrada(l):
    area = l * l 
    return area

print("área_quadrado(4) == %d" % areaQuadrada(4))
print("área_quadrado(9) == %d" % areaQuadrada(9))
