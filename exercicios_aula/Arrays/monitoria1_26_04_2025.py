# AULA 26/04/2025

# FOR / WHILE / DO WHILE  

# FOR:

# num = int(input("Digite um número: "))
# for multiplicador in range(1, 11): # estou trabalhando com o intervalo de 1 a 10
#     print(f"{num} x {multiplicador} = {num*multiplicador}")

# nome= input("Digite seu nome: ")
# for letra in nome:
#     print(letra)

# WHILE:
# O WHILE é um laço de repetição que executa enquanto a condição for verdadeira:

# Exemplo:

# while True:
#     numero = float(input("Digite um número: "))
#     if numero == 0:
#         break # o break interrompe o laço de repetição
#     print(f"Você digitou {numero}")


# Exemplo 2:
# listadeconvidados = ['Pedro', 'João', 'Maria', 'Ana']
# nome = input("Digite seu nome: ")
# while nome not in listadeconvidados:
#     print("Você não está na lista de convidados")
#     nome = input("Digite seu nome: ")   
# print("Você está na lista de convidados")

#DO WHILE:
# O DO WHILE é um laço de repetição que executa pelo menos uma vez e depois verifica a condição:

# Exemplo:
# Gere um número ineito aleatório entre 1 e 10 e peça para o usuário adivinhar o número.
# Resolução SEM função
# import random
# numero_secreto = random.randint(1, 10)
# while True:
#     tentativa = int(input("Adivinhe o número (1-10): "))
#     if tentativa == numero_secreto:
#         print("Parabéns! Você acertou!")
#         break
#     else:
#         print("Tente novamente! O número era", numero_secreto)

# Resolução COM função
# def jogo_adivinhacao():
#     import random
#     numero_secreto = random.randint(1, 10)
#     while True:
#         tentativa = int(input("Adivinhe (1-10): "))
#         if tentativa == numero_secreto:
#             return "Parabéns! Você acertou!"
#         print("Tente novamente!")
# print(jogo_adivinhacao())

#Exercício 31: Percorra uma lista de frutas e imprima cada uma.

frutas = ['maçã', 'banana', 'laranja', 'uva']
print(frutas[2][5])
