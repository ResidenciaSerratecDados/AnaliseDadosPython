## Exercício 14: Crie um menu onde o usuário pode escolher entre exibir a data, hora ou sair."""

from datetime import datetime, timezone

datahora = datetime.now()
diferenca = datahora.now().timedelta(hours=-3)
fusohorario = timezone(diferenca)
datahoraatual = datahora.astimezone(fusohorario)
data = datahoraatual.now().today()
hora = datahoraatual.now().time()

opcao = input('Escolha:\n\n1 - Data Atual\n2 - Hora Atual\n3 - Sair\n')

if opcao == 1:
  print('\nData:', data)
elif opcao == 2:
  print('\nHora:', hora)
elif opcao == 3:
  exit()
else: print('Opção Inválida. Escolha 1 ou 2 ou 3')