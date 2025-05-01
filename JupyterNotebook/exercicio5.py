## Exercício 5: Peça três números e exiba o maior.
 #Digitar 3 numeros
 #a>b>c ou a>c>b = a
 #b>a>c ou b>c>a = b
 #c>a>b ou c>b>a = c
 #a=b=c

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
print('\nO maior número é', max(num1,num2,num3))