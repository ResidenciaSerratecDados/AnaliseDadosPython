"""## Exercício 30: Crie um programa que peça 5 números e exiba apenas os números pares."""

numeros = [5]
for i in range(5):
    numeros.append(int(input('Digite um número: ')))

print('\n')
for numero in numeros:
  if numero % 2 == 0:
    print(numero)
