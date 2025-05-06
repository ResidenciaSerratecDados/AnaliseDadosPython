## Exercício 2: Peça dois números e exiba o maior.

 #Digite 2 números
 #1º numero > 2º numero -> saída: 1º número
 #1º numero < 2º numero -> saída: 2º número
 #senão, números iguais





n = float(input('Escreva o 1º número: '))
m = float(input('Escreva o 2º número: '))

print('\n')

if n > m:
  print('O maior número é: ', n)
elif n < m:
  print('O maior número é: ', m)
else:
  print('Os números são iguais: ' + str(m) + ' = ' + str(n))