"""## Exercício 25: Imprima os 10 primeiros números da sequência de Fibonacci."""

fib = [0, 1]
for _ in range(8):
    fib.append(fib[-1] + fib[-2])
print(fib)