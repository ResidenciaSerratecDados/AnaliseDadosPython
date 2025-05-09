#Lista
estados_lista = ['SP','RJ','MG']
print(estados_lista[1]) # RJ
estados_lista[1] = 'SC'
print(estados_lista) # SP, SC, MG
estados_lista.append('AC')
print(estados_lista) # SP, SC, MG, AC
estados_lista.insert(2, 'ES')
print(estados_lista) # SP, SC, ES, MG, AC
estados_lista.remove('SP')
print(estados_lista) # SC, ES, MG, AC
estados_lista.pop(1)
print(estados_lista) # SC, MG, AC

#Tupla - lista imutável - coordenadas, lista de semanas, meses
estados_tupla = ('SP','RJ','RJ') # Permite duplicatas
print(estados_lista[1]) # RJ
estados_tupla[1] = 'SC' # ERRO - Tuplas são imutáveis
estados_tupla.append('AC') # ERRO - Tuplas são imutáveis
estados_tupla.remove('SP') # ERRO - Tuplas são imutáveis

#Set
estados_set = {'SP','RJ','MG'}
print(estados_set[1]) # ERRO
estados_set.add('SC') # SP, SC, RJ, MG - ADD independemente da sequencia
estados_set.add('SC') # ERRO - Não Permite duplicatas
estados_set.remove('SP') # RJ, SC, MG

#Dicionário
estados_dict = {'SP': 'São Paulo','RJ': 'Rio de Janeiro','MG':'Minas Gerais'}
print(estados_dict['idade']) # ERRO - Esse chave não existe
print(estados_dict['RJ']) # Rio de Janeiro
estados_dict['RJ'] = 'RioJaneiro' # {'SP': 'São Paulo','RJ': 'RioJaneiro','MG':'Minas Gerais'}
estados_dict['Nome'] = 'Ana' # {'SP': 'São Paulo','RJ': 'Rio de Janeiro','MG': 'Minas Gerais', 'Nome': 'Ana'}
del estados_dict['MG'] # {'SP': 'São Paulo','RJ': 'Rio de Janeiro', 'Nome': 'Ana'}

#1- Armazene 5 frutas nas 4 estruturas
#- Array
#- estrutura de repetição
#- armazenamento (lista, tupla, set, dict)
#- print

#2- Faça o mesmo que o exercício anterior, mas com valores randômicos do tipo inteiro
#- faça o import random

########################## Lista, Tupla, Set, Dicionário
#-Acesso por índice: Lista, Dicionário, Tupla
#-Alterável: Lista, Dicionário, Set
#-Permite duplicados: Lista, Tupla
#-Ordenado: Lista, Dicionário, Tupla

#-X
x = ['maçã','banana','uva']

#-Y
y = ('maçã','banana','uva')

#-W
w = {'maçã','banana','uva'}

#-Z
z = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}