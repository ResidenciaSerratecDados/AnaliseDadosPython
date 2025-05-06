"""## Exercício 29: Imprima todas as vogais de uma string digitada pelo usuário."""

texto = input('Digite um texto: ')
for letra in texto:
  if letra in 'aeiouAEIOUáéíóúÁÉÍÓÚãõÃÕâêîôûÂÊÎÔÛÀà':
    print(letra)