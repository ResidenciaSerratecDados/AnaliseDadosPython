"""## Exercício 28: Crie um programa que solicite 5 números ao usuário e exiba a soma deles."""

soma = 0
for _ in range(5):
    soma += int(input('Digite um número: '))
   # soma = soma + int(input('Digite um número: '))
print("\nSOMA: ",soma)