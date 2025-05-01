## Exercício 15: Implemente um programa que identifica o dia da semana baseado em um número (1 = Segunda, 7 = Domingo)."""

op = input('Digite um número de 1 a 7: ')
print({
    '1':'segunda',
    '2':'terça',
    '3':'quarta',
    '4':'quinta',
    '5':'sexta',
    '6':'sábado',
    '7':'domingo'
}.get(op, 'Opção inválida'))
