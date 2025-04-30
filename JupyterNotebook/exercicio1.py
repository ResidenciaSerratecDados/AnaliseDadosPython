## Exercício 1: Verifique se um número é positivo, negativo ou zero.

 #defina um número
 #verificar se é > 0
 #> 0 -> positivo
 #< 0 -> negativo
 #caso não, 0


n = float(input('Escreva um número: '))

  if n > 0:
    print('Positivo')

  elif n < 0:
    print('Negativo')

  else:
    print('Zero')