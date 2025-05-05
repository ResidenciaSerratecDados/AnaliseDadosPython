"""## Exercício 50: Verifique se uma chave existe no dicionário."""

pessoa = {'nome': 'Estebán', 'altura': 1.76, 'idade': 21}
pessoa['nome'] = str(input('Digite o nome: '))
print('\n')

if pessoa['nome'] == 'Estebán':
    print(pessoa)
else:
    print(str(pessoa['nome']) + ' não foi encontrado no dicionário.')