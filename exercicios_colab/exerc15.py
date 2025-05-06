## Exercício 15: Implemente um programa que identifica o dia da semana baseado em um número (1 = Segunda, 7 = Domingo)."""

numero = int(input('Digite um número: '))
if numero == 1: print('1 = segunda')
elif numero == 2: print('2 = terça')
elif numero == 3: print('3 = quarta')
elif numero == 4: print('4 = quinta')
elif numero == 5: print('5 = sexta')
elif numero == 6: print('5 = sábado')
elif numero == 7: print('5 = domingo')
else: print('Opção inválida. Digite 1 ou 2 ou 3 ou 4 ou 5 ou 6 ou 7.')