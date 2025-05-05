"""## Exercício 28: Crie um programa que solicite 5 números ao usuário e exiba a soma deles."""

a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))
d = float(input('Digite o quarto número: '))
e = float(input('Digite o quinto número: '))

soma = sum([a,b,c,d,e])
print("\nSOMA: ",soma)