"""## Exercício 39: Ordene uma lista de números."""

numeros = [10]
for i in range(10):
    numeros.append(float(input('Digite um número: ')))

print('\n')
numeros.sort()
print('Lista em Ordem Crescente: ',numeros)