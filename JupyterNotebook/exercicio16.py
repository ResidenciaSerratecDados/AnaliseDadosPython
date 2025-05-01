#Exercício 16: Verifique se um número é par ou ímpar usando if ternário.

n = int(input('Escreva um número: '))
resto = (n % 2)

resultado = "É par" if resto == 0 else "É ímpar"
print(resultado)