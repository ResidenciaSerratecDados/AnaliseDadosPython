"""## Exercício 26: Percorra uma string e imprima cada caractere."""

fruta = "banana"
for letra in fruta:
    print(letra)

fruta = "banana"
indice = 0
while indice < len(fruta):
    letra = fruta[indice]
    print(letra)
    indice += 1