#5) Reescreva a função abaixo de forma a utilizar os métodos 
# de pesquisa em lista, vistos na aula passada. A função ‘enumerate’ 
# recebe uma lista como parâmetro e retorna uma lista de tuplas, 
# estas formada por pares (índice, valor). O valor ‘None’ é o valor 
# nulo da linguagem Python, similar ao ‘null’ de Java e JavaScript.

# def pesquise(lista, valor):
    #for x,e in enumerate(lista):
    		#if e == valor:
        			#return x
	#return None
 
lista = [1, 2, "Josy", "Klinsman"]

def pesquise(lista, valor):
    tuplas = []
    for x in range(len(lista)):
        if lista[x] == valor:
            tuplas.append((x, valor))
    
    if len(tuplas) == 0:
        return None
    else:
        return tuplas
    
print(pesquise(lista, 3))



