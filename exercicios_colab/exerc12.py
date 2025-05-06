## Exercício 12: Crie um menu para converter temperaturas entre Celsius, Fahrenheit e Kelvin."""

def converter(op, t):
  return {
      '1': (t*9/5) + 32,
      '2': t + 273.15
  }.get(op, 'Opção Inválida')

op = input('Digite a conversão desejada: 1-Celsius para Fahrenhet, 2-Celsius para Kelvin')
t = float(input('Digite a temperatura em Celsius: '))
print('Temperatura convertida: ', converter(op, t))