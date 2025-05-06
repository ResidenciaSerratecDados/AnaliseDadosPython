## Exercício 17: Verifique se um número é positivo ou negativo usando if ternário."""

n = float(input('Escreva um número: '))

resultado = "É posito" if n > 0 else "É negativo" if n < 0 else "Neutro"
print(resultado)