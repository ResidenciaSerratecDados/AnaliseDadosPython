"""## Exercício 42: Verifique se um número existe dentro de uma lista."""

lista = [1, 2, 3, 4, 5]

verificar = float(input('Digite um número: '))

if verificar in lista:
    print('O número ' + str(verificar) + ' está na lista.')
else:
    print('O número ' + str(verificar) + ' não está na lista.')