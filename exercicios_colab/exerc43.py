
"""## Exercício 43: Crie uma lista de números e calcule a média."""

numeros = [7]
for i in range(7):
    numeros.append(float(input('Digite um número: ')))

media = sum(numeros) / len(numeros)
print('\n')
print('Média: ',round(media,3))