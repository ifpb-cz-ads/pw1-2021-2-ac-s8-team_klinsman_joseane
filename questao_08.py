# 8) Escreva uma função que receba uma string e uma lista. A função deve comparar a string passada com os elementos da lista, também passada como parâmetro. Retorne verdadeiro se a string for encontrada dentro da lista, e falso em caso contrário.

lista = ["bom dia", "boa  noite", "boa tarde"]

def BuscarString(string, lista):
    if string in lista:
        return True
    else:
        return False
    
print(BuscarString("bom dia", lista))
