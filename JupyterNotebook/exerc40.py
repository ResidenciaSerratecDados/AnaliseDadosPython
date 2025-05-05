"""## Exercício 40: Crie uma lista com 5 números e exiba apenas os pares."""

numeros = [5]
for i in range(5):
    numeros.append(int(input('Digite um número: ')))

print('\n')
par = [i for i in numeros if i % 2 == 0]
print('Números Pares:',par)