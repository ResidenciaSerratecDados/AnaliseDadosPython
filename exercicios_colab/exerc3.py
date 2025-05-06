## Exercício 3: Verifique se um número é par ou ímpar.
  #Escrever um número
  #Função resto por 2
  #Se função resto = 0 -> é par
  #Senão -> é impar


n = int(input('Escreva um número: '))

if (n % 2) == 0:
  print('É par')
else:
  print('É impar')