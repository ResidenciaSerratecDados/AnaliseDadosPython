## Exercício 11: Crie um menu onde o usuário pode escolher entre somar, subtrair, multiplicar e dividir dois números."""

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
opcao = str(input('\nEscolha uma das operações:\n\nA - Somar\nB - Subtrair\nC - Multiplicar\nD - Dividir\n'))

if opcao == 'a' or opcao == 'A':
  soma = num1 + num2
  print('\nSoma:',soma)

elif opcao == 'b' or opcao == 'B':
  diferenca1 = num1 - num2
  diferenca2 = num2 - num1
  print('\n1ª Diferença:',diferenca1)
  print('2ª Diferença:',diferenca2)

elif opcao == 'c' or opcao == 'C':
  mult = num1 * num2
  print('\nProduto:',mult)

elif opcao == 'd' or opcao == 'D':
  quociente1 = num1 / num2 if num2 != 0 else quociente1 == 0
  quociente2 = num2 / num1 if num1 != 0 else quociente2 == 0
  print('\n1º Quociente:',quociente1)
  print('2º Quociente:',quociente2)

else:
  print('\nOpção não Encontrada. Digite A ou B ou C ou D')