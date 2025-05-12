"""## Exercício 28: Crie um programa que solicite 5 números ao usuário e exiba a soma deles."""

soma = 0
for i in range(5):
    soma += float(input('Digite um número: '))
print("\nSOMA: ",soma)