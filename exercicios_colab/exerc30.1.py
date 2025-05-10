"""## Exercício 30: Crie um programa que peça 5 números e exiba apenas os números pares."""

for _ in range(5):
  num = int(input('Digite um número: '))
  if num % 2 == 0:
    print(num)