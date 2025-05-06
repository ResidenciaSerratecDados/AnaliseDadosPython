## Exercício 19: Verifique se um número é maior que 100 e retorne 'Grande' ou 'Pequeno'."""

numero = float (input('Digite um número:'))
if numero > 100: print('Grande')
else: print('Pequeno')

numero = float (input('Digite um número:'))
resultado = 'Grande' if numero > 100 else 'Pequeno'
print(resultado)