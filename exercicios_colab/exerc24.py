"""## Exercício 24: Imprima a tabuada do 5."""

vetor = []
X = int(input('Digite um número máximo para ser multiplicado na tabuada de 5 : '))
for X in range(0,X + 1):
    mult = 5 * X
    print('5 x', X, '=', mult)