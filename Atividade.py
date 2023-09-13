"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas lista retornando uma nova lista com os valores somados
"""
listaA = list(range(1, 11))
listaB = list(range(11, 21))
lista_juntas = zip(listaA, listaB)
lista_soma = [sum((v1, v2)) for v1, v2 in list(lista_juntas)]
print(f'Soma: {lista_soma}')

