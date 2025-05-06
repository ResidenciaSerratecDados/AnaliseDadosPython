## Exercício 4: Verifique se um ano é bissexto.
  #Escrever o ano
  #Função ano por 4
  #Se função resto = 0 -> é bissexto
  #Senão -> não é bissexto
  


ano = int(input('Escreva o ano: '))
resto = int(ano % 4)
if resto == 0:
  print('É bissexto')
else:
  print('Não é bissexto')