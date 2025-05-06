## Exercício 8: Verifique se uma senha digitada corresponde a '1234'."""

senha = int(input('Digite a Senha de Login: '))
if senha == 1234:
  print('\nSenha Correta.\nO login será efetuado.')
else:
  print('\nSenha Incorreta.\nDigite novamente.')