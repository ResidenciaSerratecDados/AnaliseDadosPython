## Exercício 18: Retorne 'Adulto' se a idade for maior ou igual a 18, senão 'Menor de idade'."""

idade = int(input('Informe a idade: '))
if idade >= 18: print('Adulto')
else: print('Menor Idade')

idade = int(input('Informe a idade: '))
resultado = 'Adulto'if idade >= 18 else 'Menor Idade'
print(resultado)