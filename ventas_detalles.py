import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Si estás usando Jupyter Notebook, usa esta línea
# %matplotlib inline

# Cargar el archivo CSV
file_path = 'data/informe_cierres_caja.csv'
data = pd.read_csv(file_path)

# Verificar las primeras filas para confirmar la lectura correcta
print(data.head())

# Convertir columnas de fechas a tipo datetime
data['FechaApertura'] = pd.to_datetime(data['FechaApertura'], errors='coerce')
data['FechaCierre'] = pd.to_datetime(data['FechaCierre'], errors='coerce')

# Verificar las conversiones
print(data[['FechaApertura', 'FechaCierre']].head())

# Ejemplo 1: Distribución de Estados
estado_counts = data['Estado'].value_counts()
estado_counts.plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title('Distribución de Estados de Cajas')
plt.xlabel('Estado')
plt.ylabel('Cantidad')
plt.show()

# Ejemplo 2: Duración Promedio de Apertura de Cajas
data['Duracion_Apertura'] = (data['FechaCierre'] - data['FechaApertura']).dt.total_seconds() / 3600
data['Duracion_Apertura'].plot(kind='hist', bins=30, figsize=(10, 6), color='lightgreen')
plt.title('Duración Promedio de Apertura de Cajas (en horas)')
plt.xlabel('Duración (horas)')
plt.ylabel('Frecuencia')
plt.show()

# Ejemplo 3: Monto Total de Apertura y Diferencia por Día
data['FechaApertura_Dia'] = data['FechaApertura'].dt.date
daily_totals = data.groupby('FechaApertura_Dia')[['Monto_Apertura', 'Monto_Diferencia']].sum()
daily_totals.plot(kind='bar', figsize=(15, 7), color=['blue', 'red'])
plt.title('Monto Total de Apertura y Diferencia por Día')
plt.xlabel('Fecha')
plt.ylabel('Monto')
plt.show()

# Ejemplo 4: Rendimiento por Responsable
responsable_counts = data['Responsable'].value_counts()
responsable_counts.plot(kind='bar', figsize=(10, 6), color='orange')
plt.title('Rendimiento por Responsable')
plt.xlabel('Responsable')
plt.ylabel('Cantidad de Cajas')
plt.show()

# Ejemplo 5: Análisis de Monto Diferencia por Responsable
sns.boxplot(x='Responsable', y='Monto_Diferencia', data=data, palette='Set3', figsize=(15, 7))
plt.title('Distribución de Monto Diferencia por Responsable')
plt.xlabel('Responsable')
plt.ylabel('Monto Diferencia')
plt.xticks(rotation=45)
plt.show()
