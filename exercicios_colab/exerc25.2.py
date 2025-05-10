"""## Exercício 25: Imprima os 10 primeiros números da sequência de Fibonacci."""

fib = [0, 1]
for i in range(2, 10):
    fib.append(fib[i-1] + fib[i-2])
print(fib)