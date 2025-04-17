# Reto Técnico Interbank: Procesamiento de Transacciones Bancarias (CLI)

## 📊 Introducción
Este proyecto implementa una aplicación de línea de comandos (CLI) que procesa archivos CSV con transacciones bancarias y genera reportes detallados. La aplicación calcula el balance final (créditos menos débitos), identifica la transacción de mayor monto y proporciona un conteo por tipo de transacción, ofreciendo así una visión rápida y clara del estado financiero representado en los datos.

## 🔍 Instrucciones de Ejecución
1. Clone el repositorio:
git clone https://github.com/GinnLac/Interbank-academy-25
cd Interbank-academy-25
2. Asegúrese de tener pandas instalado:
pip install pandas
3. Ejecute la aplicación:
python Interbank.py data.csv


## 📈 Enfoque y Solución
1. Carga de datos: Importa el archivo CSV utilizando pandas, que facilita la manipulación de datos tabulares.
2. Procesamiento:
- Separa las transacciones por tipo (crédito/débito)
- Calcula sumas y balances
- Identifica valores máximos
- Cuenta ocurrencias por categoría
3. Generación de reportes: Formatea y presenta los resultados en un formato legible

## 🛠️ Herramientas utilizadas
- Python 
- Biblioteca pandas (pip install pandas)

## 📁 Estructura del proyecto
- **Interbank.py**: Contiene el codigo para cargar datos, realizar calculos y generar reportes.
- **data.csv**: Archivo con el formato requerido (id, tipo, monto).
- **README.md**: Descipción de reto.
