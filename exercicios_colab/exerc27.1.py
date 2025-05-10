"""## Exercício 27: Crie um programa que peça um número e imprima sua contagem regressiva até 0."""

contador = int(input('Digite um número máximo para a contagem regressiva: '))
for i in range(contador, -1, -1):
    print(i)