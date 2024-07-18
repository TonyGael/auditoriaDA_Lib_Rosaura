import pandas as pd

# Lee el archivo CSV guardado desde Excel
excel_csv = 'data/informe_cierres_caja.csv'

# Carga el archivo CSV en un DataFrame
df = pd.read_csv(excel_csv)

# Guarda el DataFrame como un CSV puro
puro_csv = 'data/informe_cierres_caja_clean.csv'
df.to_csv(puro_csv, index=False, encoding='utf-8')
