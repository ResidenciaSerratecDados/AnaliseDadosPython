#2- Faça o mesmo que o exercício anterior, mas com valores randômicos do tipo inteiro

#- faça o import random
import random

def gerar_dados(qtd, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(qtd)]

print('\nLista aleatória:')
lista = gerar_dados(5, 1, 22)
print(lista)

print('\nTupla aleatória:')
tupla = tuple(gerar_dados(5, 1, 22))
print(tupla)

print('\nConjunto aleatório:')
conjunto = set(gerar_dados(5, 1, 22))
print(conjunto)

print('\nDicionário Aleatório:')
dicionario = {j: valor for j, valor in enumerate(gerar_dados(5, 1, 22))}
print(dicionario)
print('\n')

########################## Lista, Tupla, Set, Dicionário

#-Acesso por índice: Lista, Dicionário, Tupla
#-Alterável: Lista, Dicionário, Set
#-Permite duplicados: Lista, Tupla
#-Ordenado: Lista, Dicionário, Tupla