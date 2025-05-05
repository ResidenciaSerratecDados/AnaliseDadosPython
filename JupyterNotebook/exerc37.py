"""## Exercício 37: Crie uma lista e inverta a ordem dos elementos."""

lista = []
for i in range(5):
    lista.append(str(input('Digite uma palavra: ')))
lista.reverse()
print('\nLista Invertida:\n')
print(lista)