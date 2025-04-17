"""
Procesador de Transacciones Bancarias

Este script procesa un archivo CSV con transacciones bancarias y genera un reporte
que incluye el balance final, la transacción de mayor monto y el conteo de transacciones.
"""
import pandas as pd

data= pd.read_csv("data.csv")

#print(data.head())

#Calculo del balance Final
debito = data.loc[data['tipo']=='Débito']
credito = data.loc[data['tipo']=='Crédito']

sum_deb = debito['monto'].sum()
sum_cre = credito['monto'].sum()

balance = sum_cre - sum_deb

#Transacción de Mayor Monto
maximo = data['monto'].max()
fila_max = data.loc[data['monto']==maximo]
max_id = fila_max['id'].values[0]

#Conteno de Transacciones
num_deb = debito['id'].count()
num_cre = credito['id'].count()

#Reporte
print("Reporte de Transacciones")
print("---------------------------------------------")
print(f"Balance Final: {balance:.2f}")
print(f"Transacción de Mayor Monto: ID {max_id} - {maximo:.2f}")
print(f"Conteo de Transacciones: Crédito: {num_cre} Débito: {num_deb}")
