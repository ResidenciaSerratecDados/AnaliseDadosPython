"""## Exercício 40: Crie uma lista com 5 números e exiba apenas os pares."""

numeros = [12, 211, 3, 700, 10]
par = [i for i in numeros if i % 2 == 0]
print(par)