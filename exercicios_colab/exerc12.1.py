## Exercício 12: Crie um menu para converter temperaturas entre Celsius, Fahrenheit e Kelvin."""

unidade = input('Escolha uma unidade de temperatura:\n\nC - Celsius\nF- Farenheit\nK - Kelvin\n')
temperatura = float(input('\n\nDigite a temperatura: '))

if unidade == 'c' or unidade == 'C':
   celsius = temperatura
   fahrenheit = (celsius * 9/5) + 32
   kelvin = celsius + 273.15

elif unidade == 'f' or unidade == 'F':
   celsius = (fahrenheit - 32) * (5/9)
   fahrenheit = temperatura
   kelvin = (fahrenheit - 32) * (5/9) + 273.15

elif unidade == 'k' or unidade == 'K':
   celsius = kelvin - 273.15
   fahrenheit = (kelvin - 273.15) * (9/5) + 32
   kelvin = temperatura

else:
  print('Opção inválida. Escolha C ou F ou K')

print('\n')
print('Temperatura em Celsius: ', round(celsius,1))
print('Temperatura em Fahrenheit: ', round(fahrenheit,1))
print('Temperatura em Kelvin: ', round(kelvin,1))