"""## Exercício 33: Multiplique cada número de uma lista por 2 e imprima o resultado."""

numeros = [5]
for i in range(5):
    numeros.append(int(input('Digite um número: ')))

print('\n')
for numero in numeros:
  mult = numero * 2
  print(str(numero) + " X " + str(2) + " = " + str(mult))
