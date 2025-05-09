import numpy as np
import array

#1- Armazene 5 frutas nas 4 estruturas

#- Lista
valores = []
    
#- estrutura de repetição
print('\n')
for i in range(5):
    valor = input(f'Digite o {i+1}º item: ')
    valores.append(valor)
    
#- armazenamento (lista, tupla, set, dict)
lista = list(valores)
tupla = tuple(valores)
conjunto = set(valores)
# dicionario = dict(valores) - ERRO - Dicionário precisa de 2 elementos chave/valor
dicionario2 = {j: valor for j, valor in enumerate(valores)}

#- print
print('\n')
print('Lista: ', lista)
print('Tupla: ', tupla)
print('Conjunto: ', conjunto)
#print('Dicionário: ', dicionario)
print('Dicionário 2: ', dicionario2)
print('\n')