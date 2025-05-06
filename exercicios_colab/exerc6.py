## Exercício 6: Verifique se um usuário pode votar (idade >= 18).
 #digite idade
 #idade >=18 -> Pode votar
 #idade < 18 -> não pode votar

idade = int(input('Informe a idade: '))

if idade >= 18:
    print('Pode votar')

else:
    print('Não pode votar')