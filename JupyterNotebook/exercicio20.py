## Exercício 20: Retorne 'Aprovado' se a nota for maior ou igual a 7, senão 'Reprovado'."""

nota = float (input('Digite a nota:'))
if 7 <= nota <= 10: print('Aprovado')
elif 0 <= nota < 7: print('Reprovado')
else: print('Valor Inválido')

nota = float(input('Digite a nota: '))
resultado = 'Aprovado' if 7 <= nota <= 10 else 'Reprovado' if 0 <= nota < 7 else 'Valor Inválido'
print(resultado)