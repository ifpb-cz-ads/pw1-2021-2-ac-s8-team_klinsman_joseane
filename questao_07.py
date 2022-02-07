#7) Escreva uma função para validar uma variável string. 
# Essa função recebe como parâmetro a string, o número 
# mínimo e máximo de caracteres. Retorne verdadeiro se o 
# tamanho da string estiver entre os valores de máximo e mínimo, 
# e falso em caso contrário.

def validarStr(string, min, max):
    tam = len(string)
    if(tam >= min and tam <= max):
        return True
    else:
        return False
    
print(validarStr("Klinsman", 1, 4))
