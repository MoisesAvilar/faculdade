import pandas as pd


# Importando o arquivo

df = pd.read_csv('table.csv')

# Imprime o setor e a quantidade

compras_por_setor = df['SETOR'].value_counts()
print(compras_por_setor)
