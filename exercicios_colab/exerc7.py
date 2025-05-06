## Exercício 7: Verifique se já posso ir embora da aula de Análise de Dados sem assinar a folha.
 #digitar hora atual
 #ver se a hora atual >= estipulda
 #se for, pode sair
 #senão, não pode sair

from datetime import datetime, time

print(datetime.now().time())
if datetime.now().time() >= time(00,45,0):
  print('Pode')
else:
  print('Não pode')

diferenca = timedelta(hours=-3)
print(diferenca)