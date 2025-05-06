"""## Exercício 36: Crie uma lista com 5 números e imprima o maior."""

numeros = [5]
for i in range(5):
    numeros.append(int(input('Digite um número: ')))

print('\n')
print('Maior número:',max(numeros))