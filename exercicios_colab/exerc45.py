"""## Exercício 45: Crie uma lista de números e remova os duplicados."""

lista = []
for i in range(8):
    lista.append(float(input('Digite um número: ')))
    lista_sem_duplicatas = list(set(lista))

print('\n')
print(lista_sem_duplicatas)