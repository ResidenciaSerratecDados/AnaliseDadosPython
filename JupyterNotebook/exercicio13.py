## Exercício 13: Crie um programa que traduza números de 1 a 5 para palavras (1 = um, 2 = dois...)."""

numero = int(input('Digite um número: '))
if numero == 1: print('1 = um')
elif numero == 2: print('2 = dois')
elif numero == 3: print('3 = três')
elif numero == 4: print('4 = quatro')
elif numero == 5: print('5 = cinco')
else: print('Opção inválida. Digite 1 ou 2 ou 3 ou 4 ou 5.')