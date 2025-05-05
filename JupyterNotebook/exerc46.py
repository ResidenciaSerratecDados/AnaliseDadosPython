"""## Exercício 46: Crie um dicionário com nomes de alunos e suas notas e exiba a nota de um aluno específico."""

# Criação do dicionário com nomes de alunos e suas notas
notas_alunos = {
    "João": 8.5,
    "Maria": 9.2,
    "José": 7.8,
    "Ana": 10.0
}

# Escolhe um nome de aluno para buscar a nota
nome_aluno = str(input('Digite o nome do aluno: '))

# Verifica se o nome do aluno existe no dicionário
if nome_aluno in notas_alunos:
    # Se existir, imprime a nota do aluno
    print('A nota de ' +str(nome_aluno) + ' é: ' + str(notas_alunos[nome_aluno]))
else:
    # Se não existir, informa que o aluno não foi encontrado
    print('Aluno ' + str(nome_aluno) + ' não encontrado no dicionário.')