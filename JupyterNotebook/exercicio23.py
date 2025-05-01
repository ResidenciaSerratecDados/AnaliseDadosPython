## Exercício 23: Calcule a soma dos números de 1 a 100."""

vetor = []
for X in range(1,101):
    vetor = (vetor + [X])
    soma = sum(vetor)
print(soma)