import pandas as pd

#serie = pd.Series([10, 20, 30]) #estrutura unidimensional de vetores
#print(serie)

dados = {
    'nome': ['Ana', 'Bia', 'Carlos'],
    'idade': [30, 10, 18]
}
df = pd.DataFrame(dados) #estrutura bidimensional de matriz
print(df)