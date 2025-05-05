"""## Exercício 44: Crie uma lista de nomes e converta todos para maiúsculas."""

lista = []
for i in range(5):
    lista.append(str(input('Digite uma palavra: ')))
    lista[i] = lista[i].upper()

print('\n')
print(lista)