import pandas as pd

# leemos el archivo csv del cliente
chunk_df = pd.read_csv('./data/ventas.csv', chunksize=1000)

# mostramos informaciion de las pruiemras filas del DataFrame
for chunk in chunk_df:
    print(chunk.head())
    break
