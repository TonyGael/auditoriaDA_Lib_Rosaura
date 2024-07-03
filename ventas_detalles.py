import pandas as pd

# leemos el archivo csv del cliente
df = pd.read_csv('./data/ventas.csv')

# mostramos informaciion de las pruiemras filas del DataFrame
print(df.head())
