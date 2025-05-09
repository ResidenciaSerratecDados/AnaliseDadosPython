#2- Faça o mesmo que o exercício anterior, mas com valores randômicos do tipo inteiro

#- faça o import random
import random

def gerar_dados(qtd, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(qtd)]

dados = gerar_dados(5, 1, 22)
lista = list(dados)
tupla = tuple(dados)
conjunto = set(dados)
dicionario = {j: valor for j, valor in enumerate(dados)}

print('\nLista:',lista)
print('\nTupla:',tupla)
print('\nConjunto:',conjunto)
print('\nDicionário:', dicionario)
print('\n')

########################## Lista, Tupla, Set, Dicionário

#-Acesso por índice: Lista, Dicionário, Tupla
#-Alterável: Lista, Dicionário, Set
#-Permite duplicados: Lista, Tupla
#-Ordenado: Lista, Dicionário, Tupla